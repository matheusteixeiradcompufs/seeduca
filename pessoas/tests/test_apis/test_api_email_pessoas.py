from pessoas.models import EmailPessoa
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class EmailPessoaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(EmailPessoaAPITest, self).setUp()

        self.basenamelist = 'pessoas:email-api-list'
        self.basenamedetail = 'pessoas:email-api-detail'

        self.data_instance = {
            'endereco': 'teste@email.com',
            'pessoa': self.aluno,
        }

        self.data_instance2 = {
            'endereco': 'teste2@email.com',
            'pessoa': self.aluno.id,
        }

        self.data_instance_update = {
            'endereco': 'teste3@email.com',
        }

        self.instance = EmailPessoa.objects.create(**self.data_instance)
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