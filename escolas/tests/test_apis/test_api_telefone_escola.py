from escolas.models import TelefoneEscola
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class TelefoneEscolaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(TelefoneEscolaAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-telefone-api-list'
        self.basenamedetail = 'escolas:escola-telefone-api-detail'

        self.data_instance = {
            'numero': '77777777777',
            'escola': self.escola,
        }

        self.data_instance2 = {
            'numero': '77777777778',
            'escola': self.escola.id,
        }

        self.data_instance_update = {
            'numero': '77777777779',
        }

        self.instance = TelefoneEscola.objects.create(**self.data_instance)
        return supersetup

    def test_list_telefone_escola(self):
        self.list_base(self.basenamelist)

    def test_create_telefone_escola(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_telefone_escola(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_telefone_escola(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_telefone_escola(self):
        self.destroy_base(self.instance.id, self.basenamedetail)