from pessoas.models import Boletim
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class BoletimAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(BoletimAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-boletim-api-list'
        self.basenamedetail = 'pessoas:aluno-boletim-api-detail'

        self.data_instance = {
            'ano': 2000,
            'aluno': self.aluno,
        }

        self.data_instance2 = {
            'ano': 2001,
            'aluno': self.aluno.id,
        }

        self.data_instance_update = {
            'ano': 2002,
        }

        self.instance = Boletim.objects.create(**self.data_instance)
        return supersetup

    def test_list_boletim_aluno(self):
        self.list_base(self.basenamelist)

    def test_create_boletim_aluno(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_boletim_aluno(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_boletim_aluno(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_boletim_aluno(self):
        self.destroy_base(self.instance.id, self.basenamedetail)