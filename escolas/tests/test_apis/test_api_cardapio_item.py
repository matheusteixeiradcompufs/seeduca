from escolas.models import ItemCardapioMerenda
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class ItemCardapioAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(ItemCardapioAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-cardapio-item-api-list'
        self.basenamedetail = 'escolas:escola-cardapio-item-api-detail'

        self.data_instance = {
            'nome': 'Teste',
            'descricao': 'Descricao Teste',
        }

        self.data_instance2 = {
            'nome': 'Teste 2',
            'descricao': 'Descricao Teste 2',
        }

        self.data_instance_update = {
            'descricao': 'Descricao Atualizada',
        }

        self.instance = ItemCardapioMerenda.objects.create(**self.data_instance)
        return supersetup

    def test_list_cardapio_item(self):
        self.list_base(self.basenamelist)

    def test_create_cardapio_item(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_cardapio_item(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_cardapio_item(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_cardapio_item(self):
        self.destroy_base(self.instance.id, self.basenamedetail)