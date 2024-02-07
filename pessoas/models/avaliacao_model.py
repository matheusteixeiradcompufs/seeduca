from django.db import models

from escolas.models import Disciplina, Turma
from pessoas.models.aluno_model import Aluno
from pessoas.models.boletim_model import Boletim


class Avaliacao(models.Model):
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
    )
    nota = models.FloatField(
        default=0,
    )
    finalizada = models.BooleanField(
        default=False,
    )
    criada_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizada_em = models.DateTimeField(
        auto_now=True,
    )
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_avaliacoes',
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE,
        related_name='disciplina_avaliacoes',
    )
    boletim = models.ForeignKey(
        Boletim,
        on_delete=models.CASCADE,
        related_name='boletim_avaliacoes',
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='turma_avaliacoes',
    )

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'

    def save(self, *args, **kwargs):
        avaliacao = super().save(*args, **kwargs)
        if self.nome == 'A1':
            self.boletim.boletim_medias.filter(tipo='M1').update(valor=self.nota)
        if self.nome in ['A2', 'R1']:
            self.boletim.boletim_medias.filter(tipo='M1').update(
                valor=(self.boletim.boletim_medias.get(tipo='M1').valor + self.nota) / 2
            )
        if self.nome == 'A3':
            self.boletim.boletim_medias.filter(tipo='M2').update(valor=self.nota)
        if self.nome in ['A4', 'R2']:
            media_m2 = self.boletim.boletim_medias.get(tipo='M2').valor
            self.boletim.boletim_medias.filter(tipo='M2').update(valor=(media_m2 + self.nota) / 2)
            media_mg = (self.boletim.boletim_medias.get(tipo='M1').valor + media_m2) / 2
            self.boletim.boletim_medias.filter(tipo='MG').update(valor=media_mg)
        return avaliacao

    # def save(self, *args, **kwargs):
    #     avaliacao = super().save(*args, **kwargs)
    #     if self.name == 'A1':
    #         self.boletim.boletim_medias[0].valor = self.nota
    #     if self.name in ['A2', 'R1']:
    #         self.boletim.boletim_medias[0].valor = (self.boletim.boletim_medias[0].valor + self.nota) / 2
    #     if self.name == 'A3':
    #         self.boletim.boletim_medias[1].valor = self.nota
    #     if self.name in ['A4', 'R2']:
    #         self.boletim.boletim_medias[1].valor = (self.boletim.boletim_medias[1].valor + self.nota) / 2
    #         self.boletim.boletim_medias[2].valor = (self.boletim.boletim_medias[0].valor + self.boletim.boletim_medias[1].valor) / 2
    #     return avaliacao
