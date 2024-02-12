from django.db import models
from django.core.exceptions import ValidationError

from escolas.models import Disciplina
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
    confirmar = models.BooleanField(
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

    def __str__(self):
        return self.get_nome_display()

    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'

    def save(self, *args, **kwargs):

        if self.pk:
            if not self.boletim.encerrar:
                situacao = self.boletim.boletim_situacoes.filter(disciplina=self.disciplina).first()
                if not situacao.situacao:
                    avaliacoes = self.boletim.boletim_avaliacoes.filter(disciplina=self.disciplina)
                    a1 = avaliacoes.filter(nome='A1').first()
                    a2 = avaliacoes.filter(nome='A2').first()
                    r1 = avaliacoes.filter(nome='R1').first()
                    media = self.boletim.boletim_medias.filter(tipo='M1', disciplina=self.disciplina.id).first()
                    if not a1.confirmar and not a2.confirmar and not r1.confirmar:
                        media.valor = 0
                    elif a1.confirmar and not a2.confirmar and not r1.confirmar:
                        media.valor = a1.nota
                    elif a1.confirmar and a2.confirmar and not r1.confirmar:
                        media.valor = (a1.nota + a2.nota) / 2
                    elif a1.confirmar and a2.confirmar and r1.confirmar:
                        if r1.nota > (a1.nota + a2.nota) / 2:
                            media.valor = ((a1.nota + a2.nota) + 2 * r1.nota) / 4
                        else:
                            media.valor = (a1.nota + a2.nota) / 2
                    else:
                        raise ValidationError('Existem avaliações dessa matéria pendentes de confirmação no 1º semestre')

                    media.save()

                    a3 = avaliacoes.filter(nome='A3').first()
                    a4 = avaliacoes.filter(nome='A4').first()
                    r2 = avaliacoes.filter(nome='R2').first()
                    media = self.boletim.boletim_medias.filter(tipo='M2', disciplina=self.disciplina.id).first()
                    if not a3.confirmar and not a4.confirmar and not r2.confirmar:
                        media.valor = 0
                    elif a3.confirmar and not a4.confirmar and not r2.confirmar:
                        media.valor = a3.nota
                    elif a3.confirmar and a4.confirmar and not r2.confirmar:
                        media.valor = (a3.nota + a4.nota) / 2
                    elif a3.confirmar and a4.confirmar and r2.confirmar:
                        if r2.nota > (a3.nota + a4.nota) / 2:
                            media.valor = ((a3.nota + a4.nota) + 2 * r2.nota) / 4
                        else:
                            media.valor = (a3.nota + a4.nota) / 2
                    else:
                        raise ValidationError('Existem avaliações dessa matéria pendentes de confirmação no 2º semestre')

                    media.save()
                else:
                    raise ValidationError('As notas de uma matéria finalizada não podem mais ser editadas!')
            else:
                raise ValidationError('Os boletins encerrados não podem mais ser editados!')

        return super().save(*args, **kwargs)

