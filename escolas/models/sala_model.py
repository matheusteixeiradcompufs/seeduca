from django.db import models

from escolas.models.escola_model import Escola


class Sala(models.Model):
    numero = models.IntegerField()
    quantidade_alunos = models.IntegerField(
        default=0,
    )
    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='escola_salas',
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return '{:03}'.format(self.numero)

    class Meta:
        unique_together = ['numero', 'escola']

    def save(self, *args, **kwargs):
        quantidade_anterior = 0

        if self.pk:
            # Se a instância já existe, obter a quantidade anterior de alunos
            sala_anterior = Sala.objects.get(pk=self.pk)
            quantidade_anterior = sala_anterior.quantidade_alunos

        # Salvar a instância
        super(Sala, self).save(*args, **kwargs)

        # Atualizar a quantidade de alunos na escola
        diferenca_quantidade = self.quantidade_alunos - quantidade_anterior
        self.escola.quantidade_alunos += diferenca_quantidade
        self.escola.save()

        # Atualizar o número de salas na escola
        self.escola.num_salas = self.escola.escola_salas.count()
        self.escola.save()

        return

