from pessoas.models import Transporte
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class TransporteAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(TransporteAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-transporte-api-list'
        self.basenamedetail = 'pessoas:aluno-transporte-api-detail'

        self.data_instance = {
            'placa': 'AAA0000',
            'ano': 2023,
        }

        self.data_instance2 = {
            'placa': 'AAA0001',
            'ano': 2023,
        }

        self.data_instance_update = {
            'ano': 2024,
        }

        self.instance = Transporte.objects.create(**self.data_instance)
        return supersetup

    def test_list_transporte_aluno(self):
        self.list_base(self.basenamelist)

    def test_create_transporte_aluno(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_transporte_aluno(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_transporte_aluno(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_transporte_aluno(self):
        self.destroy_base(self.instance.id, self.basenamedetail)