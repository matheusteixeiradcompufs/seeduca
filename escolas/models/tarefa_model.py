from django.db import models

from escolas.models.dia_agenda_model import DiaAgenda

class Tarefa(models.Model):
    """
    Representa uma tarefa a ser realizada.

    Cada tarefa possui um nome, uma descrição, um tipo (escola ou casa), data e hora de cadastro,
    data e hora de atualização, uma data de entrega (opcional) e está associada a um dia específico da agenda.
    """

    TAREFA_CHOICES = [
        ('E', 'Escola'),
        ('C', 'Casa'),
    ]
    """
    Escolhas de tipo de tarefa.
    """

    nome = models.CharField(
        max_length=100,
    )
    """
    O nome da tarefa.
    """

    descricao = models.TextField()
    """
    A descrição da tarefa.
    """

    tipo = models.CharField(
        max_length=10,
        choices=TAREFA_CHOICES,
    )
    """
    O tipo de tarefa (escola ou casa).
    """

    cadastrada_em = models.DateTimeField(
        auto_now_add=True,
    )
    """
    A data e hora de cadastro da tarefa, preenchida automaticamente no momento da criação.
    """

    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    """
    A data e hora da última atualização da tarefa, atualizada automaticamente sempre que a tarefa é modificada.
    """

    entrega = models.DateTimeField(
        blank=True,
        null=True,
    )
    """
    A data e hora de entrega da tarefa (opcional).
    """

    diaAgenda = models.ForeignKey(
        DiaAgenda,
        verbose_name='dia da agenda',
        on_delete=models.PROTECT,
        related_name='dia_tarefas',
    )
    """
    O dia da agenda ao qual esta tarefa está associada.
    """

    def __str__(self):
        """
        Retorna uma representação legível do nome da tarefa.

        Returns:
            str: O nome da tarefa.
        """
        return str(self.nome)
