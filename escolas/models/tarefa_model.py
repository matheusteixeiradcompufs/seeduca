from django.db import models

from escolas.models.dia_agenda_model import DiaAgenda


class Tarefa(models.Model):
    TAREFA_CHOICES = [
        ('E', 'Escola'),
        ('C', 'Casa'),
    ]

    nome = models.CharField(
        max_length=100,
    )
    descricao = models.TextField()
    tipo = models.CharField(
        max_length=10,
        choices=TAREFA_CHOICES,
    )
    cadastrada_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    entrega = models.DateTimeField(
        blank=True,
        null=True,
    )
    diaAgenda = models.ForeignKey(
        DiaAgenda,
        verbose_name='dia da agenda',
        on_delete=models.PROTECT,
        related_name='dia_tarefas',
    )

    def __str__(self):
        return str(self.nome)