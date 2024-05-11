from django.db import models
from pessoas.models.frequencia_model import Frequencia


class DiaLetivo(models.Model):
    """
    Model para representar um dia letivo de uma frequência de aluno.

    Atributos:
        data (DateField): A data do dia letivo.
        presenca (BooleanField): Um campo booleano que indica se o aluno esteve presente no dia letivo.
        frequencia (ForeignKey): A referência à frequência do aluno associada ao dia letivo.
        criado_em (DateTimeField): O timestamp de quando o dia letivo foi criado.
        atualizado_em (DateTimeField): O timestamp de quando o dia letivo foi atualizado.
    """

    data = models.DateField(verbose_name='data')
    presenca = models.BooleanField(
        default=True,
        verbose_name='presença'
    )

    frequencia = models.ForeignKey(
        Frequencia,
        on_delete=models.CASCADE,
        related_name='frequencia_diasletivos',
        verbose_name='frequência'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='criado em'
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='atualizado em'
    )

    def __str__(self):
        """
        Retorna uma representação legível do dia letivo.

        Returns:
            str: A representação do dia letivo.
        """
        return str(self.data)

    class Meta:
        verbose_name = 'dia letivo'
        verbose_name_plural = 'dias letivos'
        unique_together = ['data', 'frequencia']

    def save(self, *args, **kwargs):
        """
        Salva o objeto e atualiza o percentual de frequência associado à frequência do aluno.

        Args:
            args: Argumentos posicionais.
            kwargs: Argumentos de palavra-chave.
        """
        # Chama o método save do modelo pai
        super().save(*args, **kwargs)

        # Calcula o novo percentual de frequência do aluno
        total_dias_letivos = self.frequencia.frequencia_diasletivos.count()
        presenca_true_count = self.frequencia.frequencia_diasletivos.filter(presenca=True).count()

        # Evita a divisão por zero
        percentual = (presenca_true_count / total_dias_letivos) * 100 if total_dias_letivos > 0 else 0

        # Atualiza o percentual no modelo Frequencia
        self.frequencia.percentual = percentual
        self.frequencia.save()

    def delete(self, *args, **kwargs):
        """
        Exclui o objeto e atualiza o percentual de frequência associado à frequência do aluno.

        Args:
            args: Argumentos posicionais.
            kwargs: Argumentos de palavra-chave.
        """
        # Antes de excluir o objeto, atualize o percentual de frequência
        super().delete(*args, **kwargs)

        # Obtém a frequência associada ao dia letivo
        frequencia = self.frequencia

        # Calcula o novo percentual de frequência do aluno
        total_dias_letivos = frequencia.frequencia_diasletivos.count()
        presenca_true_count = frequencia.frequencia_diasletivos.filter(presenca=True).count()

        # Evita a divisão por zero
        percentual = (presenca_true_count / total_dias_letivos) * 100 if total_dias_letivos > 0 else 0

        # Atualiza o percentual no modelo Frequencia
        frequencia.percentual = percentual
        frequencia.save()
