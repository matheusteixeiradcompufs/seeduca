from escolas.models import Sala
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class SalaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(SalaAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-sala-api-list'
        self.basenamedetail = 'escolas:escola-sala-api-detail'

        self.data_instance = {
            'numero': 0,
            'escola': self.escola,
        }

        self.data_instance2 = {
            'numero': 1,
            'escola': self.escola.id,
        }

        self.data_instance_update = {
            'quantidade_alunos': 20,
        }

        self.instance = Sala.objects.create(**self.data_instance)
        return supersetup

    def test_list_sala(self):
        self.list_base(self.basenamelist)

    def test_create_sala(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_sala(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_sala(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_sala(self):
        self.destroy_base(self.instance.id, self.basenamedetail)