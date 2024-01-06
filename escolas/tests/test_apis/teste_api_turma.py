from escolas.models import Turma, Sala
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class TurmaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(TurmaAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-sala-turma-api-list'
        self.basenamedetail = 'escolas:escola-sala-turma-api-detail'

        self.data_instance = {
            'nome': 'Teste',
            'ano': 2000,
            'turno': 'Teste',
            'sala': Sala.objects.create(
                numero=1,
                escola=self.escola
            ),
        }

        self.data_instance2 = {
            'nome': 'Teste2',
            'ano': 2000,
            'turno': 'Teste',
            'sala': Sala.objects.create(
                numero=2,
                escola=self.escola
            ).id,
        }

        self.data_instance_update = {
            'ano': 2001,
        }

        self.instance = Turma.objects.create(**self.data_instance)
        return supersetup

    def test_list_turma(self):
        self.list_base(self.basenamelist)

    def test_create_turma(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_turma(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_turma(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_turma(self):
        self.destroy_base(self.instance.id, self.basenamedetail)