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
    """
    Função para gerar um token JWT com base nos dados fornecidos.

    Args:
        ano_turma (str): O ano da turma.
        turma (str): O nome da turma.
        escola (str): O nome da escola.
        nome (str): O primeiro nome do aluno.
        sobrenome (str): O sobrenome do aluno.
        matricula (str): O número de matrícula do aluno.

    Returns:
        str: O token JWT gerado.
    """
    data_validade = f'{ano_turma}-12-31'
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
    """
    Model para representar o boletim de um aluno em uma turma.

    Atributos:
        status (CharField): O status do boletim.
        encerrar (BooleanField): Um campo booleano que indica se o boletim foi encerrado.
        token (CharField): O token JWT associado ao boletim.
        qr_code (ImageField): O código QR gerado para o boletim.
        turma (ForeignKey): A referência à turma associada ao boletim.
        aluno (ForeignKey): A referência ao aluno associado ao boletim.
    """

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
        verbose_name='status'
    )

    encerrar = models.BooleanField(
        default=False,
        verbose_name='encerrado'
    )

    token = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name='token'
    )

    qr_code = models.ImageField(
        upload_to='boletins_qr_codes/',
        null=True,
        blank=True,
        verbose_name='código QR'
    )

    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='turma_boletins',
        verbose_name='turma'
    )

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_boletins',
        verbose_name='aluno'
    )

    def __str__(self):
        """
        Retorna uma representação legível do boletim.

        Returns:
            str: A representação do boletim.
        """
        return f'Boletim de {str(self.aluno.usuario.first_name)} da turma {self.turma}'

    class Meta:
        verbose_name_plural = 'boletins'
        unique_together = ['aluno', 'turma']

    def delete(self, *args, **kwargs):
        """
        Exclui o arquivo de QR code associado ao boletim.

        Args:
            args: Argumentos posicionais.
            kwargs: Argumentos de palavra-chave.
        """
        os.remove(os.path.join(settings.MEDIA_ROOT, self.qr_code.name))
        super(Boletim, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        Salva o boletim e gera o token JWT e o código QR associado.

        Raises:
            ValidationError: Se ocorrerem erros durante a validação.
        """
        # Verifica se o boletim já estava criado antes de salvar
        if not self.pk:
            # Se o boletim não estava criado
            super().save(*args, **kwargs)

            # Pega todas as disciplinas da turma
            disciplinas_da_turma = self.turma.disciplinas.all()

            # Itera sobre cada disciplina da turma
            for disciplina in disciplinas_da_turma:
                # Cria um objeto Situacao para cada disciplina
                from pessoas.models import Situacao
                Situacao.objects.create(
                    disciplina=disciplina,
                    boletim=self,
                )

                # Cria os três tipos de media para cada disciplina
                from pessoas.models.media_model import Media
                for tipo_media, _ in Media.TIPO_MEDIA_CHOICES:
                    Media.objects.create(
                        tipo=tipo_media,
                        disciplina=disciplina,
                        boletim=self
                    )

                # Cria os seis tipos de avaliacoes para cada disciplina
                from pessoas.models.avaliacao_model import Avaliacao
                for tipo_avaliacao, _ in Avaliacao.TIPO_AVALIACAO_CHOICES:
                    Avaliacao.objects.create(
                        nome=tipo_avaliacao,
                        aluno=self.aluno,
                        disciplina=disciplina,
                        boletim=self,
                    )

            # Cria uma frequencia para o boletim cadastrado
            from pessoas.models.frequencia_model import Frequencia
            Frequencia.objects.create(
                boletim=self,
            )

            # Cria uma agenda de recados para o boletim cadastrado
            from pessoas.models.agenda_recados_model import AgendaRecados
            AgendaRecados.objects.create(
                boletim=self,
            )

            # Gera um token para o boletim cadastrado
            self.token = gerar_token(
                self.turma.ano,
                self.turma.nome,
                self.turma.sala.escola.nome,
                self.aluno.usuario.first_name,
                self.aluno.usuario.last_name,
                self.aluno.matricula,
            )

            token = self.token

            # Gera a imagem de GR Code para o token criado
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
            # Se o boletim já estava criado
            # Verifica se a opção encerrar está marcada
            if self.encerrar:
                # Se encerrar está marcado
                situacoes = self.boletim_situacoes.filter(finalizar=False)
                # Verifica se todas as situações das disciplinas já estão finalizadas
                if situacoes.count() == 0:
                    # Se todas as disciplinas ja foram finalizadas
                    # Filtra todas as matérias que estão com situação 'R' (Reprovada)
                    materias_reprovadas = self.boletim_situacoes.filter(situacao='R')
                    # Se não tem matéria reprovada e a frequência é maior que 75%
                    if materias_reprovadas.count() == 0 and self.boletim_frequencia.percentual >= 75:
                        # Status do boletim recebe 'A' (Aprovado)
                        self.status = 'A'
                    # Senão
                    # Se somente o percentual da frequência for maior que 75%
                    elif self.boletim_frequencia.percentual >= 75:
                        # Status do boletim recebe 'RM' (Reprovado por média)
                        self.status = 'RM'
                    # Senão
                    # Se somente não tem matérias reprovadas
                    elif materias_reprovadas.count() == 0:
                        # Status do boletim recebe 'RF' (Reprovado por falta)
                        self.status = 'RF'
                    # Senão
                    else:
                        # Status do boletim recebe 'RFM' (Reprovado por falta e por média'
                        self.status = 'RFM'
                else:
                    # Se todas as disciplinas não foram finalizadas
                    raise ValidationError('Alguma matéria ainda não foi finalizada!')
            else:
                # Se o encerrar não está marcado o status do boletim fica em 'M' (Matriculado)
                self.status = 'M'
            return super(Boletim, self).save(*args, **kwargs)
