from django.urls import reverse
from rest_framework import status

from escolas.models import Sala, Turma, Disciplina, AgendaEscolar
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class AgendaDisciplinasAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        super(AgendaDisciplinasAPITest, self).setUp()
        self.disciplina1 = Disciplina.objects.create(nome="Teste1")
        self.disciplina2 = Disciplina.objects.create(nome="Teste2")
        turma = Turma.objects.create(
            nome="Turma Teste",
            ano=2024,
            turno="M",
            sala=Sala.objects.create(
                numero=10,
                escola=self.escola
            )
        )
        turma.disciplinas.add(self.disciplina1)
        turma.disciplinas.add(self.disciplina2)
        self.agenda = AgendaEscolar.objects.create(
            turma=turma
        )

    def test_if_agenda_disciplinas_returns_status_201(self):
        data = {
            "agenda_id": self.agenda.id,
            "seg": [self.disciplina1.id],
            "ter": [self.disciplina2.id],
            "qua": [self.disciplina1.id, self.disciplina2.id],
            "qui": [self.disciplina1.id, self.disciplina2.id],
            "sex": [self.disciplina1.id, self.disciplina2.id],
        }
        url = reverse("pessoas:agenda_disciplinas")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_agenda_disciplinas_returns_status_400(self):
        data = {
            "agenda_id": self.agenda.id,
            "seg": [self.disciplina1.id],
            "ter": [self.disciplina2.id],
            "qua": [self.disciplina1.id, self.disciplina2.id],
            "qui": [self.disciplina1.id, self.disciplina2.id],
            "sex": [self.disciplina1.id, "self.disciplina2.id"],
        }
        url = reverse("pessoas:agenda_disciplinas")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_agenda_disciplinas_returns_status_validation_error(self):
        data = {
            "agenda_id": 10,
            "seg": [self.disciplina1.id],
            "ter": [self.disciplina2.id],
            "qua": [self.disciplina1.id, self.disciplina2.id],
            "qui": [self.disciplina1.id, self.disciplina2.id],
            "sex": [self.disciplina1.id, self.disciplina2.id],
        }
        url = reverse("pessoas:agenda_disciplinas")
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            str(response.data['agenda_id'][0]),
            "Agenda não encontrada."
        )