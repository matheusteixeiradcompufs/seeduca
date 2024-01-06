from escolas.models import AgendaEscolar, Turma, Sala
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class AgendaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(AgendaAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-sala-turma-agenda-api-list'
        self.basenamedetail = 'escolas:escola-sala-turma-agenda-api-detail'

        self.data_instance = {
            'turma': Turma.objects.create(
                nome='Teste1',
                ano=2001,
                turno='Teste1',
                sala=Sala.objects.create(
                    numero=2,
                    escola=self.escola
                ),
            )
        }

        self.data_instance2 = {
            'turma': Turma.objects.create(
                nome='Teste2',
                ano=2002,
                turno='Teste2',
                sala=Sala.objects.create(
                    numero=3,
                    escola=self.escola
                ),
            ).id
        }

        self.data_instance_update = {
            'turno': Turma.objects.create(
                nome='Teste4',
                ano=2004,
                turno='Teste4',
                sala=Sala.objects.create(
                    numero=4,
                    escola=self.escola
                ),
            ).id
        }

        self.instance = AgendaEscolar.objects.create(**self.data_instance)
        return supersetup

    def test_list_agenda(self):
        self.list_base(self.basenamelist)

    def test_create_agenda(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_agenda(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_agenda(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_agenda(self):
        self.destroy_base(self.instance.id, self.basenamedetail)