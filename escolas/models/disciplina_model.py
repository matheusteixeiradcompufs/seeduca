from django.db import models

class Disciplina(models.Model):
    """
    Representa uma disciplina escolar.

    Uma disciplina é identificada pelo seu nome, que deve ser único.
    """

    nome = models.CharField(
        max_length=100,
        unique=True,
    )
    """
    O nome da disciplina.
    """

    def __str__(self):
        """
        Retorna uma representação legível do nome da disciplina.

        Returns:
            str: O nome da disciplina.
        """
        return str(self.nome)
