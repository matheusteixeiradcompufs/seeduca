import os
import jwt
from io import BytesIO
import qrcode
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.db import models
from appseeduca import settings
from escolas.models import Turma
from pessoas.models.aluno_model import Aluno


def gerar_token(ano_turma, turma, escola, nome, sobrenome, matricula):
    data_validade = f'{ano_turma}-{12}-{31}'
    payload = {
        'val': data_validade,
        'tur': turma,
        'esc': escola,
        'nom': nome,
        'sob': sobrenome,
        'mat': matricula,
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")


class Boletim(models.Model):
    STATUS_CHOICES = [
        ('A', 'Aprovado'),
        ('M', 'Matriculado'),
        ('T', 'Transferido'),
        ('RM', 'Reprovado por média'),
        ('RF', 'Reprovado por falta'),
        ('RFM', 'Reprovado por falta e por média'),
    ]

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='M',
    )
    encerrar = models.BooleanField(
        default=False,
    )
    token = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
    )
    qr_code = models.ImageField(
        upload_to='boletins_qr_codes/',
        null=True,
        blank=True,
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='turma_boletins',
    )
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_boletins',
    )

    def __str__(self):
        return f'Boletim de {str(self.aluno.usuario.first_name)} da turma {self.turma}'

    class Meta:
        verbose_name_plural = 'boletins'
        unique_together = ['aluno', 'turma']

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.qr_code.name))
        super(Boletim, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.pk:

            super().save(*args, **kwargs)

            from pessoas.models.avaliacao_model import Avaliacao
            from pessoas.models.media_model import Media
            from pessoas.models.frequencia_model import Frequencia
            from pessoas.models.agenda_recados_model import AgendaRecados

            disciplinas_da_turma = self.turma.disciplinas.all()

            for disciplina in disciplinas_da_turma:
                from pessoas.models import Situacao
                Situacao.objects.create(
                    disciplina=disciplina,
                    boletim=self,
                )

                # Cria as médias (M1, M2, MG)
                for tipo_media, _ in Media.TIPO_MEDIA_CHOICES:
                    Media.objects.create(
                        tipo=tipo_media,
                        disciplina=disciplina,
                        boletim=self
                    )

                # Cria as avaliações (A1, A2, R1, A3, A4, R2)
                for tipo_avaliacao, _ in Avaliacao.TIPO_AVALIACAO_CHOICES:
                    Avaliacao.objects.create(
                        nome=tipo_avaliacao,
                        aluno=self.aluno,
                        disciplina=disciplina,
                        boletim=self,
                    )

            Frequencia.objects.create(
                boletim=self,
            )

            AgendaRecados.objects.create(
                boletim=self,
            )

            self.token = gerar_token(
                self.turma.ano,
                self.turma.nome,
                self.turma.sala.escola.nome,
                self.aluno.usuario.first_name,
                self.aluno.usuario.last_name,
                self.aluno.matricula,
            )

            token = self.token
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(token)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            qr_img.save(buffer, format='PNG')
            self.qr_code.save(f'qr_code_{self.aluno.id}_{self.turma.ano}.png', ContentFile(buffer.getvalue()), save=False)
            self.save()
        else:
            if self.encerrar:
                situacoes = self.boletim_situacoes.filter(finalizar=False)
                if situacoes.count() == 0:
                    materias_reprovadas = self.boletim_situacoes.filter(situacao='R')
                    if materias_reprovadas.count() == 0 and self.boletim_frequencia.percentual >= 75:
                        self.status = 'A'
                    elif self.boletim_frequencia.percentual >= 75:
                        self.status = 'RM'
                    elif materias_reprovadas.count() == 0:
                        self.status = 'RF'
                    else:
                        self.status = 'RFM'
                else:
                    raise ValidationError('Alguma matéria ainda não foi finalizada!')
            else:
                self.status = 'M'
            return super(Boletim, self).save(*args, **kwargs)