import calendar
from datetime import date

from django.db import models
from escolas.models.turma_model import Turma


class AgendaEscolar(models.Model):
    """
    Representa a agenda escolar associada a uma turma.

    Atributos:
        turma (ForeignKey): A turma associada à agenda escolar.
    """
    turma = models.OneToOneField(
        Turma,
        on_delete=models.CASCADE,
        related_name='turma_agenda',
        verbose_name='Turma'
    )

    def __str__(self):
        """
        Retorna uma representação legível da agenda escolar.
        """
        return 'Agenda do ' + str(self.turma)

    class Meta:
        """
        Metadados para a classe AgendaEscolar.
        """
        verbose_name = 'agenda escolar'
        verbose_name_plural = 'agendas escolares'

    def save(self, *args, **kwargs):
        """
        Salva a agenda e cria dias úteis associados a ela se ainda não existirem.

        Se não houver dias associados a esta agenda, cria dias úteis para o ano da turma.
        """
        super().save(*args, **kwargs)

        # Verifica se já existem dias associados a esta agenda
        if not self.agenda_dias.exists():
            # Obtém o ano da turma
            ano_turma = self.turma.ano

            # Preenche os dias úteis do ano da turma
            dias = self.get_dias_do_ano(ano_turma)
            for dia in dias:
                from escolas.models import DiaAgenda
                DiaAgenda.objects.create(data=dia[0], util=dia[1], agenda=self)

    @staticmethod
    def get_dias_do_ano(ano):
        """
        Obtém uma lista de tuplas representando os dias úteis e não úteis de um ano.

        Args:
            ano (int): O ano para o qual os dias devem ser obtidos.

        Returns:
            list: Uma lista de tuplas contendo objetos date e um booleano indicando se o dia é útil.
        """
        dias = []
        # Itera sobre todos os meses do ano
        for mes in range(1, 13):
            # Obtém o último dia do mês
            ultimo_dia_mes = calendar.monthrange(ano, mes)[1]
            # Itera sobre todos os dias do mês
            for dia in range(1, ultimo_dia_mes + 1):
                data = date(ano, mes, dia)
                # Verifica se o dia é útil (não é sábado nem domingo)
                if data.weekday() < 5:
                    dias.append((data, True))
                else:
                    dias.append((data, False))
        return dias
