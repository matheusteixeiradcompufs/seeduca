from django.db import models
from django.core.exceptions import ValidationError
from escolas.models import Disciplina
from pessoas.models.aluno_model import Aluno
from pessoas.models.boletim_model import Boletim


class Avaliacao(models.Model):
    """
    Model para representar uma avaliação de um aluno em uma disciplina.

    Atributos:
        nome (CharField): O nome da avaliação.
        nota (FloatField): A nota obtida na avaliação.
        confirmar (BooleanField): Um campo booleano que indica se a avaliação foi confirmada.
        criada_em (DateTimeField): A data e hora de criação da avaliação.
        atualizada_em (DateTimeField): A data e hora de atualização da avaliação.
        aluno (ForeignKey): A referência ao aluno associado à avaliação.
        disciplina (ForeignKey): A referência à disciplina associada à avaliação.
        boletim (ForeignKey): A referência ao boletim associado à avaliação.
    """

    TIPO_AVALIACAO_CHOICES = [
        ('A1', '1ª Avaliação'),
        ('A2', '2ª Avaliação'),
        ('R1', '1ª Recuperação'),
        ('A3', '3ª Avaliação'),
        ('A4', '4ª Avaliação'),
        ('R2', '2ª Recuperação'),
    ]

    nome = models.CharField(
        max_length=100,
        choices=TIPO_AVALIACAO_CHOICES,
        verbose_name='tipo de avaliação'
    )

    nota = models.FloatField(
        default=0,
        verbose_name='nota'
    )

    confirmar = models.BooleanField(
        default=False,
        verbose_name='confirmada'
    )

    criada_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='criada em'
    )

    atualizada_em = models.DateTimeField(
        auto_now=True,
        verbose_name='atualizada em'
    )

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_avaliacoes',
        verbose_name='aluno'
    )

    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='disciplina_avaliacoes',
        verbose_name='disciplina'
    )

    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_avaliacoes',
        verbose_name='boletim'
    )

    def __str__(self):
        """
        Retorna uma representação legível de uma avaliação.

        Retorna:
            str: A representação da avaliação.
        """
        return f'{self.get_nome_display()} - {self.disciplina.nome}'

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'

    def save(self, *args, **kwargs):
        """
        Salva a avaliação e atualiza a média do boletim relacionado.

        Raises:
            ValidationError: Se ocorrerem erros durante a validação.
        """
        if self.pk:
            super_save = super().save(*args, **kwargs)
            # Verifica se o boletim está encerrado ou não
            if not self.boletim.encerrar:
                # Se o boletim não foi encerrado
                situacao = self.boletim.boletim_situacoes.filter(disciplina=self.disciplina).first()
                # Verifica se a disciplina foi finalizada no boletim
                if situacao.situacao is None:
                    # Se a disciplina não foi finalizada
                    avaliacoes = self.boletim.boletim_avaliacoes.filter(disciplina=self.disciplina)
                    a1 = avaliacoes.filter(nome='A1').first()
                    a2 = avaliacoes.filter(nome='A2').first()
                    r1 = avaliacoes.filter(nome='R1').first()

                    # Calcula a média da 1ª unidade a medida que as notas das avaliações são confirmadas
                    media = self.boletim.boletim_medias.filter(tipo='M1', disciplina=self.disciplina.id).first()
                    if not a1.confirmar and not a2.confirmar and not r1.confirmar:
                        # Se nenhuma nota de uma materia do primeiro semestre foi confirmada a média é 0
                        media.valor = 0
                    elif a1.confirmar and not a2.confirmar and not r1.confirmar:
                        # Se somente a primeira avaliação foi confirmada a média será igual à 1ª avaliação
                        media.valor = a1.nota
                    elif a1.confirmar and a2.confirmar and not r1.confirmar:
                        # Se somente a 1ª e a 2ª avaliação forem confirmadas a média será igual à média das duas
                        media.valor = (a1.nota + a2.nota) / 2
                    elif a1.confirmar and a2.confirmar and r1.confirmar:
                        # Se a 1ª, 2ª e 1ª recuperação forem confirmadas a média será igual à média entre a
                        # 1ª recuperação e a média da 1ª e 2ª avaliações

                        # Verifica se a nota da 1ª recuperação é maior que a média
                        if r1.nota > (a1.nota + a2.nota) / 2:
                            # Se for maior a nota da 1ª recuperação é considerada pra calcular a média
                            media.valor = ((a1.nota + a2.nota) + 2 * r1.nota) / 4
                        else:
                            # Se for menor a 1ª recuperação é descartada
                            media.valor = (a1.nota + a2.nota) / 2
                    else:
                        # Em qualquer outra combinação entre as confirmações de notas
                        raise ValidationError(
                            'Existem avaliações dessa matéria pendentes de confirmação no 1º semestre')

                    media.save()

                    a3 = avaliacoes.filter(nome='A3').first()
                    a4 = avaliacoes.filter(nome='A4').first()
                    r2 = avaliacoes.filter(nome='R2').first()

                    # Calcula a média da 2ª unidade a medida que as notas das avaliações são confirmadas
                    media = self.boletim.boletim_medias.filter(tipo='M2', disciplina=self.disciplina.id).first()
                    if not a3.confirmar and not a4.confirmar and not r2.confirmar:
                        # Se nenhuma nota de uma materia do segundo semestre foi confirmada a média é 0
                        media.valor = 0
                    elif a3.confirmar and not a4.confirmar and not r2.confirmar:
                        # Se somente a 3ª avaliação foi confirmada a média será igual à 3ª avaliação
                        media.valor = a3.nota
                    elif a3.confirmar and a4.confirmar and not r2.confirmar:
                        # Se somente a 3ª e a 4ª avaliação forem confirmadas a média será igual à média das duas
                        media.valor = (a3.nota + a4.nota) / 2
                    elif a3.confirmar and a4.confirmar and r2.confirmar:
                        # Se a 3ª, 4ª e 2ª recuperação forem confirmadas a média será igual à média entre a
                        # 2ª recuperação e a média da 3ª e 4ª avaliações

                        # Verifica se a nota da 2ª recuperação é maior que a média
                        if r2.nota > (a3.nota + a4.nota) / 2:
                            # Se for maior a nota da 2ª recuperação é considerada pra calcular a média
                            media.valor = ((a3.nota + a4.nota) + 2 * r2.nota) / 4
                        else:
                            # Se for menor a 2ª recuperação é descartada
                            media.valor = (a3.nota + a4.nota) / 2
                    else:
                        # Em qualquer outra combinação entre as confirmações de notas
                        raise ValidationError(
                            'Existem avaliações dessa matéria pendentes de confirmação no 2º semestre')
                    # Salvar média
                    media.save()

                else:
                    # Se a disciplina foi finalizada
                    raise ValidationError('As notas de uma matéria finalizada não podem mais ser editadas!')
            else:
                # Se o boletim foi encerrado
                raise ValidationError('Os boletins encerrados não podem mais ser editados!')
            return super_save
        else:
            return super().save(*args, **kwargs)
