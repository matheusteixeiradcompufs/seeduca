from escolas.models import CardapioMerenda
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class CardapioAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(CardapioAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-cardapio-api-list'
        self.basenamedetail = 'escolas:escola-cardapio-api-detail'

        self.data_instance = {
            'data': '2000-01-01',
            'turno': 'teste',
            'escola': self.escola,
        }

        self.data_instance2 = {
            'data': '2000-01-02',
            'turno': 'teste',
            'escola': self.escola.id,
        }

        self.data_instance_update = {
            'turno': 'teste2',
        }

        self.instance = CardapioMerenda.objects.create(**self.data_instance)
        return supersetup

    def test_list_cardapio(self):
        self.list_base(self.basenamelist)

    def test_create_cardapio(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_cardapio(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_cardapio(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_cardapio(self):
        self.destroy_base(self.instance.id, self.basenamedetail)