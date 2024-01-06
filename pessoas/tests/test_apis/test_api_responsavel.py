from pessoas.models import Responsavel
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class ResponsavelAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(ResponsavelAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-responsavel-api-list'
        self.basenamedetail = 'pessoas:aluno-responsavel-api-detail'

        self.data_instance = {
            'cpf': '22222222222',
            'nome': 'Nome Teste',
            'observacao': 'Observacao teste',
            'aluno': self.aluno,
        }

        self.data_instance2 = {
            'cpf': '22222222223',
            'nome': 'Nome Teste2',
            'observacao': 'Observacao teste2',
            'aluno': self.aluno.id,
        }

        self.data_instance_update = {
            'nome': 'Novo Nome',
        }

        self.instance = Responsavel.objects.create(**self.data_instance)
        return supersetup

    def test_list_responsavel_pessoa(self):
        self.list_base(self.basenamelist)

    def test_create_responsavel_pessoa(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_responsavel_pessoa(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_responsavel_pessoa(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_responsavel_pessoa(self):
        self.destroy_base(self.instance.id, self.basenamedetail)