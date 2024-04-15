from django.db import models
from rest_framework.exceptions import ValidationError

from escolas.models import Disciplina
from pessoas.models.boletim_model import Boletim


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
        if self.pk:
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