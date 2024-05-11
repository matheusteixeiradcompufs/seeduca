from django.db import models
from threadlocals.threadlocals import get_current_request

from pessoas.models import Pessoa, Aluno
from pessoas.models.agenda_recados_model import AgendaRecados


class Recado(models.Model):
    """
    Modelo que representa um recado.

    Atributos:
        texto (TextField): O texto do recado.
        eh_aluno (BooleanField): Indica se o remetente do recado é um aluno.
        publicado_em (DateTimeField): Data e hora de publicação do recado.
        atualizado_em (DateTimeField): Data e hora de atualização do recado.
        pessoa (ForeignKey): A pessoa que enviou o recado.
        agenda (ForeignKey): A agenda de recados associada ao recado.
    """

    texto = models.TextField(
        verbose_name='texto'
    )
    eh_aluno = models.BooleanField(
        default=False,
        verbose_name='é aluno'
    )
    publicado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='publicado em'
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='atualizado em'
    )
    pessoa = models.ForeignKey(
        Pessoa,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='pessoa_recados',
        verbose_name='pessoa'
    )
    agenda = models.ForeignKey(
        AgendaRecados,
        on_delete=models.CASCADE,
        related_name='agenda_recados',
        verbose_name='agenda'
    )

    def __str__(self):
        """
        Retorna uma representação legível do recado.

        Returns:
            str: Uma string representando o recado.
        """
        return f'Recado de {self.pessoa} em {self.publicado_em}'

    def save(self, *args, **kwargs):
        """
        Salva o objeto Recado.

        Verifica se o remetente do recado é um aluno e define a pessoa que enviou o recado
        com base no usuário logado.

        Returns:
            model: O objeto Recado salvo.
        """
        request = get_current_request()

        # Verifica se o remetente do recado é um aluno
        self.eh_aluno = Aluno.objects.filter(usuario=request.user).exists()

        # Define a pessoa que enviou o recado com base no usuário logado
        if not request.user.is_superuser:
            self.pessoa = Pessoa.objects.get(usuario=request.user)

        return super(Recado, self).save(*args, **kwargs)
