from escolas.models import Disciplina
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class DisciplinaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(DisciplinaAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-disciplina-api-list'
        self.basenamedetail = 'escolas:escola-disciplina-api-detail'

        self.data_instance = {
            'nome': 'Disciplina',
        }

        self.data_instance2 = {
            'nome': 'Disciplina2',
        }

        self.data_instance_update = {
            'nome': 'Disciplina3',
        }

        self.instance = Disciplina.objects.create(**self.data_instance)
        return supersetup

    def test_list_disciplina(self):
        self.list_base(self.basenamelist)

    def test_create_disciplina(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_disciplina(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_disciplina(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_disciplina(self):
        self.destroy_base(self.instance.id, self.basenamedetail)