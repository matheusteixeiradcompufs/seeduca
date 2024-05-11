from django.core.exceptions import ValidationError
from django.db import models

from escolas.models import Disciplina
from pessoas.models.boletim_model import Boletim


class Situacao(models.Model):
    """
    Modelo que representa a situação de uma disciplina em um boletim.

    Atributos:
        situacao (CharField): A situação da disciplina (Aprovado ou Reprovado).
        finalizar (BooleanField): Indica se a situação está finalizada.
        disciplina (ForeignKey): A disciplina associada à situação.
        boletim (ForeignKey): O boletim associado à situação.
    """

    SITUACAO_CHOICES = [
        ('A', 'Aprovado'),
        ('R', 'Reprovado'),
    ]

    situacao = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=SITUACAO_CHOICES,
        verbose_name='situação'
    )
    finalizar = models.BooleanField(
        default=False,
        verbose_name='finalizar'
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='disciplina_situacoes',
        verbose_name='disciplina'
    )
    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_situacoes',
        verbose_name='boletim'
    )

    def __str__(self):
        """
        Retorna uma representação legível da situação.

        Returns:
            str: Uma string representando a situação.
        """
        return f'Situação de {self.disciplina}'

    class Meta:
        verbose_name = 'situação'
        verbose_name_plural = 'situações'

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para verificar e atualizar a situação do boletim.

        Raises:
            ValidationError: Se houver tentativa de finalizar uma disciplina sem todas as notas confirmadas.
        """
        # Verifica se a situação já existe
        if self.pk:
            # Se a situação já existe
            # Verifica se o boletim está encerrado
            if not self.boletim.encerrar:
                # Se o boletim não está encerrado
                # Verifica se a situação da disciplina está marcada como finalizar
                if self.finalizar:
                    # Se finalizar estiver marcada
                    avaliacoes = self.boletim.boletim_avaliacoes.filter(disciplina=self.disciplina.id)
                    a1 = avaliacoes.filter(nome='A1').first()
                    a2 = avaliacoes.filter(nome='A2').first()
                    r1 = avaliacoes.filter(nome='R1').first()
                    a3 = avaliacoes.filter(nome='A3').first()
                    a4 = avaliacoes.filter(nome='A4').first()
                    r2 = avaliacoes.filter(nome='R2').first()
                    # Verificar se todas as avaliações estão confirmadas
                    if not a1.confirmar or not a2.confirmar or not a3.confirmar or \
                            not a4.confirmar or not r1.confirmar or not r2.confirmar:
                        # Levantar um erro se alguma matéria não estiver confirmada
                        raise ValidationError('Só é possível finalizar uma matéria quando '
                                              'todas as notas do ano forem confirmadas')

                    # pegar ou calcular os valores das médias
                    m1 = self.boletim.boletim_medias.filter(tipo='M1', disciplina=self.disciplina.id).first()
                    m1 = m1.valor if m1 else 0
                    m2 = self.boletim.boletim_medias.filter(tipo='M2', disciplina=self.disciplina.id).first()
                    m2 = m2.valor if m2 else 0
                    mg = self.boletim.boletim_medias.filter(tipo='MG', disciplina=self.disciplina.id).first()
                    mg.valor = (m1 + m2) / 2
                    mg.save()

                    # média geral é maior ou igual a 5
                    if mg.valor >= 5:
                        # situação recebe 'A' (Aprovado)
                        self.situacao = 'A'
                    else:
                        # situação recebe 'R' (Reprovado)
                        self.situacao = 'R'
                else:
                    # Se não estiver marcada apagar o valor de situação e zerar a média geral
                    self.situacao = None
                    mg = self.boletim.boletim_medias.filter(tipo='MG', disciplina=self.disciplina.id).first()
                    mg.valor = 0
                    mg.save()
            else:
                # Se o boletim estiver encerrado
                raise ValidationError('Os boletins encerrados não podem mais ser editados!')
        return super().save(*args, **kwargs)
