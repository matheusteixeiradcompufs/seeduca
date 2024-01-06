from pessoas.models import TelefonePessoa
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class TelefonePessoaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(TelefonePessoaAPITest, self).setUp()

        self.basenamelist = 'pessoas:telefone-api-list'
        self.basenamedetail = 'pessoas:telefone-api-detail'

        self.data_instance = {
            'numero': '99999999999',
            'pessoa': self.aluno,
        }

        self.data_instance2 = {
            'numero': '99999999997',
            'pessoa': self.aluno.id,
        }

        self.data_instance_update = {
            'numero': '99999999998',
        }

        self.instance = TelefonePessoa.objects.create(**self.data_instance)
        return supersetup

    def test_list_email_pessoa(self):
        self.list_base(self.basenamelist)

    def test_create_email_pessoa(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_email_pessoa(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_email_pessoa(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_email_pessoa(self):
        self.destroy_base(self.instance.id, self.basenamedetail)