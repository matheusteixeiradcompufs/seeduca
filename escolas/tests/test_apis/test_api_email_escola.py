from escolas.models import EmailEscola
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class EmailEscolaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(EmailEscolaAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-email-api-list'
        self.basenamedetail = 'escolas:escola-email-api-detail'

        self.data_instance = {
            'endereco': 'endereco@teste.com',
            'escola': self.escola,
        }

        self.data_instance2 = {
            'endereco': 'endereco2@teste.com',
            'escola': self.escola.id,
        }

        self.data_instance_update = {
            'endereco': 'endereco3@teste.com',
        }

        self.instance = EmailEscola.objects.create(**self.data_instance)
        return supersetup

    def test_list_email_escola(self):
        self.list_base(self.basenamelist)

    def test_create_email_escola(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_email_escola(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_email_escola(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_email_escola(self):
        self.destroy_base(self.instance.id, self.basenamedetail)