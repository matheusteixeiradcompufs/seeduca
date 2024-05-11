from django.db import models

class Escola(models.Model):
    """
    Representa uma escola.

    Uma escola é identificada pelo CNPJ único e possui informações como nome, endereço, número de salas,
    quantidade de alunos, descrição, data de criação, data de atualização e uma imagem opcional.
    """

    cnpj = models.CharField(
        max_length=14,
        unique=True,
    )
    """
    O CNPJ da escola, único para cada escola.
    """

    nome = models.CharField(
        max_length=100,
    )
    """
    O nome da escola.
    """

    endereco = models.CharField(
        max_length=255,
    )
    """
    O endereço da escola.
    """

    num_salas = models.IntegerField(
        default=0,
    )
    """
    O número de salas na escola.
    """

    quantidade_alunos = models.IntegerField(
        default=0,
    )
    """
    A quantidade de alunos na escola.
    """

    descricao = models.TextField(
        blank=True,
        null=True,
    )
    """
    Uma descrição opcional da escola.
    """

    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    """
    A data e hora de criação da escola, preenchida automaticamente no momento da criação.
    """

    atualizado_em = models.DateTimeField(
        auto_now=True,
    )
    """
    A data e hora da última atualização da escola, atualizada automaticamente sempre que a escola é modificada.
    """

    imagem = models.ImageField(
        upload_to='escolas_images/',
        blank=True,
        null=True,
        default='',
    )
    """
    Uma imagem opcional da escola.
    """

    def __str__(self):
        """
        Retorna uma representação legível do nome da escola.

        Returns:
            str: O nome da escola.
        """
        return str(self.nome)
