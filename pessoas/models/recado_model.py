from django.db import models
from threadlocals.threadlocals import get_current_request

from pessoas.models import Pessoa, Aluno
from pessoas.models.agenda_recados_model import AgendaRecados


class Recado(models.Model):
    texto = models.TextField()
    eh_aluno = models.BooleanField(
        default=False,
    )
    publicado_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    pessoa = models.ForeignKey(
        Pessoa,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='pessoa_recados',
    )
    agenda = models.ForeignKey(
        AgendaRecados,
        on_delete=models.CASCADE,
        related_name='agenda_recados',
    )

    def __str__(self):
        return f'Recado de {self.pessoa} em {self.publicado_em}'

    def save(self, *args, **kwargs):

        request = get_current_request()

        self.eh_aluno = Aluno.objects.filter(usuario=request.user).exists()

        if not request.user.is_superuser:
            self.pessoa = Pessoa.objects.get(usuario=request.user)

        return super(Recado, self).save()
