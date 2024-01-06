from escolas.models import Escola
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class EscolaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(EscolaAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-api-list'
        self.basenamedetail = 'escolas:escola-api-detail'

        self.data_instance = {
            'cnpj': '11111111111111',
            'nome': 'Nome Teste',
            'endereco': 'Endereço Teste',
        }

        self.data_instance2 = {
            'cnpj': '11111111111112',
            'nome': 'Nome Teste 2',
            'endereco': 'Endereço Teste 2',
        }

        self.data_instance_update = {
            'endereco': 'Atualizado',
        }

        self.instance = Escola.objects.create(**self.data_instance)
        return supersetup

    def test_list_escola(self):
        self.list_base(self.basenamelist)

    def test_create_escola(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_escola(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_escola(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_escola(self):
        self.destroy_base(self.instance.id, self.basenamedetail)