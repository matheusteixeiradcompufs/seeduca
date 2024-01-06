from escolas.models import DiaAgenda, AgendaEscolar, Turma, Sala
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class DiaAgendaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(DiaAgendaAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-sala-turma-agenda-dia-api-list'
        self.basenamedetail = 'escolas:escola-sala-turma-agenda-dia-api-detail'

        self.data_instance = {
            'data': '2000-01-02',
            'agenda': AgendaEscolar.objects.create(
                turma=Turma.objects.create(
                    nome='Teste1',
                    ano=2001,
                    turno='Teste1',
                    sala=Sala.objects.create(
                        numero=2,
                        escola=self.escola
                    ),
                )
            )
        }

        self.data_instance2 = {
            'data': '2000-01-03',
            'agenda': AgendaEscolar.objects.create(
                turma=Turma.objects.create(
                    nome='Teste2',
                    ano=2001,
                    turno='Teste1',
                    sala=Sala.objects.create(
                        numero=3,
                        escola=self.escola
                    ),
                )
            ).id
        }

        self.data_instance_update = {
            'data': '2001-02-01',
        }

        self.instance = DiaAgenda.objects.create(**self.data_instance)
        return supersetup

    def test_list_dia_agenda(self):
        self.list_base(self.basenamelist)

    def test_create_dia_agenda(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_dia_agenda(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_dia_agenda(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_dia_agenda(self):
        self.destroy_base(self.instance.id, self.basenamedetail)