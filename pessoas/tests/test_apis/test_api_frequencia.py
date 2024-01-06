from pessoas.models import Frequencia
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class FrequenciaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(FrequenciaAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-frequencia-api-list'
        self.basenamedetail = 'pessoas:aluno-frequencia-api-detail'

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

        self.instance = Frequencia.objects.create(**self.data_instance)
        return supersetup

    def test_list_frequencia_aluno(self):
        self.list_base(self.basenamelist)

    def test_create_frequencia_aluno(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_frequencia_aluno(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_frequencia_aluno(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_frequencia_aluno(self):
        self.destroy_base(self.instance.id, self.basenamedetail)