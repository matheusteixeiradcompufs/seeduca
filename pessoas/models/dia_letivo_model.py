from django.db import models

from pessoas.models.frequencia_model import Frequencia


class DiaLetivo(models.Model):
    data = models.DateField()
    presenca = models.BooleanField(
        default=True,
    )
    frequencia = models.ForeignKey(
        Frequencia,
        on_delete=models.CASCADE,
        related_name='frequencia_diasletivos',
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
    )
    atualizado_em = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return str(self.data)

    class Meta:
        verbose_name = 'dia letivo'
        verbose_name_plural = 'dias letivos'
        unique_together = ['data', 'frequencia']

    def save(self, *args, **kwargs):
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