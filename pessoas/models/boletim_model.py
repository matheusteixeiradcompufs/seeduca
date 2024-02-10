from django.db import models
from rest_framework.exceptions import ValidationError

from escolas.models import YearField, Disciplina
from pessoas.models.frequencia_model import Frequencia
from pessoas.models.aluno_model import Aluno


class Boletim(models.Model):
    STATUS_CHOICES = [
        ('A', 'Aprovado'),
        ('M', 'Matriculado'),
        ('T', 'Transferido'),
        ('RM', 'Reprovado por média'),
        ('RF', 'Reprovado por falta'),
        ('RFM', 'Reprovado por falta e por média'),
    ]
    ano = YearField()
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='M',
    )
    encerrar = models.BooleanField(
        default=False,
    )
    frequencia = models.OneToOneField(
        Frequencia,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='frequencia_boletim',
    )
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_boletins',
    )

    def __str__(self):
        return 'Boletim de ' + str(self.aluno.usuario.first_name) + ' em ' + str(self.ano)

    class Meta:
        verbose_name_plural = 'boletins'
        unique_together = ['ano', 'aluno']

    def save(self, *args, **kwargs):

        if not self.pk:
            # Verifica se o aluno está matriculado em alguma turma do mesmo ano
            if not self.aluno.turmas.filter(ano=self.ano).exists():
                raise ValueError(f"O aluno {self.aluno} não está matriculado em nenhuma turma do ano {self.ano}.")

            super().save(*args, **kwargs)

            # Obtém a turma do aluno do mesmo ano do boletim
            turmas_do_aluno = self.aluno.turmas.filter(ano=self.ano)

            from pessoas.models.avaliacao_model import Avaliacao
            from pessoas.models.media_model import Media
            for turma in turmas_do_aluno:
                disciplinas_da_turma = turma.disciplinas.all()

                for disciplina in disciplinas_da_turma:
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
                            turma=turma
                        )
        else:
            if self.encerrar:
                situacoes = self.boletim_situacoes.filter(finalizar=False)
                if situacoes.count() == 0:
                    materias_reprovadas = self.boletim_situacoes.filter(situacao='R')
                    if materias_reprovadas.count() == 0 and self.frequencia.percentual >= 75:
                        self.status = 'A'
                    elif self.frequencia.percentual >= 75:
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


class Situacao(models.Model):
    SITUACAO_CHOICES = [
        ('A', 'Aprovado'),
        ('R', 'Reprovado'),
    ]

    situacao = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=SITUACAO_CHOICES,
    )
    finalizar = models.BooleanField(
        default=False
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='disciplina_situacoes',
    )
    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_situacoes'
    )

    def __str__(self):
        return f'Situação de {self.disciplina}'

    class Meta:
        verbose_name = 'situação'
        verbose_name_plural = 'situações'

    def save(self, *args, **kwargs):
        if not self.boletim.encerrar:
            if self.finalizar:
                avaliacoes = self.boletim.boletim_avaliacoes.filter(disciplina=self.disciplina.id)
                a1 = avaliacoes.filter(nome='A1').first()
                a2 = avaliacoes.filter(nome='A2').first()
                r1 = avaliacoes.filter(nome='R1').first()
                a3 = avaliacoes.filter(nome='A3').first()
                a4 = avaliacoes.filter(nome='A4').first()
                r2 = avaliacoes.filter(nome='R2').first()
                if not a1.confirmar or not a2.confirmar or not a3.confirmar or \
                        not a4.confirmar or not r1.confirmar or not r2.confirmar:
                    raise ValidationError('Só é possível finalizar uma materia quando '
                                          'todas as notas do ano forem confirmadas')

                m1 = self.boletim.boletim_medias.filter(tipo='M1', disciplina=self.disciplina.id).first()
                m1 = m1.valor if m1 else 0
                m2 = self.boletim.boletim_medias.filter(tipo='M2', disciplina=self.disciplina.id).first()
                m2 = m2.valor if m2 else 0
                mg = self.boletim.boletim_medias.filter(tipo='MG', disciplina=self.disciplina.id).first()
                mg.valor = (m1 + m2) / 2
                mg.save()
                if mg.valor >= 5:
                    self.situacao = 'A'
                else:
                    self.situacao = 'R'
            else:
                self.situacao = None
                mg = self.boletim.boletim_medias.filter(tipo='MG', disciplina=self.disciplina.id).first()
                mg.valor = 0
                mg.save()
        else:
            raise ValidationError('Os boletins encerrados não podem mais ser editados!')
        return super().save(*args, **kwargs)