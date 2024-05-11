from django.db import models


class YearField(models.IntegerField):
    """
    Um campo personalizado para armazenar anos.

    Este campo é uma subclasse de IntegerField, que limita os valores possíveis a um intervalo de anos de 1900 a 2100.
    """

    def __init__(self, *args, **kwargs):
        """
        Inicializa o YearField.

        Este método define validadores vazios e escolhas como uma lista de tuplas contendo anos de 1900 a 2100.

        Args:
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        kwargs['validators'] = []
        kwargs['choices'] = [(i, i) for i in range(1900, 2101)]
        super().__init__(*args, **kwargs)


class Telefone(models.Model):
    """
    Representa um número de telefone.
    """
    numero = models.CharField(
        max_length=20,
    )

    def __str__(self):
        """
        Retorna uma representação legível do número de telefone.
        """
        return str(self.numero)


class Email(models.Model):
    """
    Representa um endereço de email.
    """
    endereco = models.EmailField()

    def __str__(self):
        """
        Retorna uma representação legível do endereço de email.
        """
        return str(self.endereco)


class AvisoBase(models.Model):
    """
    Modelo base para avisos.

    Este modelo contém informações básicas de um aviso, como título, texto, data de publicação e data de atualização.
    """
    titulo = models.CharField(
        max_length=100,
    )
    """
    O título do aviso.
    """
    texto = models.TextField()
    """
    O texto do aviso.
    """
    publicado_em = models.DateTimeField(
        auto_now_add=True,
    )
    """
    A data e hora de publicação do aviso, preenchida automaticamente no momento da criação.
    """
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    """
    A data e hora da última atualização do aviso, atualizada automaticamente sempre que o aviso é modificado.
    """
