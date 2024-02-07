import calendar
from datetime import date

from django.db import models

from escolas.models.turma_model import Turma


class AgendaEscolar(models.Model):
    turma = models.OneToOneField(
        Turma,
        on_delete=models.CASCADE,
        related_name='turma_agenda',
    )

    def __str__(self):
        return 'Agenda do ' + str(self.turma)

    class Meta:
        verbose_name = 'agenda escolar'
        verbose_name_plural = 'agendas escolares'

    def save(self, *args, **kwargs):
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