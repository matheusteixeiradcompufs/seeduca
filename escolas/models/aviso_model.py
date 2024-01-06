from django.db import models

from escolas.models.dia_agenda_model import DiaAgenda


class Aviso(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    publicado_em = models.DateTimeField(auto_now_add=True)
    diaAgenda = models.ForeignKey(DiaAgenda, verbose_name='dia da agenda', on_delete=models.CASCADE, related_name='dia_avisos')

    def __str__(self):
        return str(self.titulo)