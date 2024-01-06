from django.db import models

from escolas.models.dia_agenda_model import DiaAgenda


class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.BooleanField(default=False)
    cadastrada_em = models.DateTimeField(auto_now_add=True)
    entrega = models.DateTimeField(blank=True, null=True)
    diaAgenda = models.ForeignKey(DiaAgenda, verbose_name='dia da agenda', on_delete=models.CASCADE, related_name='dia_tarefas')

    def __str__(self):
        return str(self.nome)