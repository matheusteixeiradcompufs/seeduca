from django.db import models

from escolas.models import YearField
from pessoas.models.aluno_model import Aluno


class Boletim(models.Model):
    ano = YearField()
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='aluno_boletins',
    )

    def __str__(self):
        return 'Boletim de ' + str(self.aluno.usuario.first_name) + ' em ' + str(self.ano)

    class Meta:
        verbose_name_plural = 'boletins'
        unique_together = ['ano', 'aluno']

    def save(self, *args, **kwargs):

        if not self.pk:
            # Verifica se o aluno está matriculado em alguma turma do mesmo ano
            if not self.aluno.turmas.filter(ano=self.ano).exists():
                raise ValueError(f"O aluno {self.aluno} não está matriculado em nenhuma turma do ano {self.ano}.")

            super().save(*args, **kwargs)

            # Obtém a turma do aluno do mesmo ano do boletim
            turmas_do_aluno = self.aluno.turmas.filter(ano=self.ano)

            from pessoas.models.avaliacao_model import Avaliacao
            from pessoas.models.media_model import Media
            for turma in turmas_do_aluno:
                disciplinas_da_turma = turma.disciplinas.all()

                for disciplina in disciplinas_da_turma:
                    # Cria as avaliações (A1, A2, R1, A3, A4, R2)
                    for tipo_avaliacao, _ in Avaliacao.TIPO_AVALIACAO_CHOICES:
                        Avaliacao.objects.create(
                            nome=tipo_avaliacao,
                            aluno=self.aluno,
                            disciplina=disciplina,
                            boletim=self,
                            turma=turma
                        )

                    # Cria as médias (M1, M2, MG)
                    for tipo_media, _ in Media.TIPO_MEDIA_CHOICES:
                        Media.objects.create(
                            tipo=tipo_media,
                            disciplina=disciplina,
                            boletim=self
                        )
        else:
            super().save(*args, **kwargs)