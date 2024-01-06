from pessoas.models import DiaLetivo, Frequencia
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class DiaLetivoAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(DiaLetivoAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-frequencia-dialetivo-api-list'
        self.basenamedetail = 'pessoas:aluno-frequencia-dialetivo-api-detail'

        frequencia = Frequencia.objects.create(
            ano=2000,
            aluno=self.aluno
        )

        self.data_instance = {
            'data': '2023-12-30',
            'frequencia': frequencia,
        }

        self.data_instance2 = {
            'data': '2023-12-31',
            'frequencia': frequencia.id,
        }

        self.data_instance_update = {
            'ano': '2024-01-02',
        }

        self.instance = DiaLetivo.objects.create(**self.data_instance)
        return supersetup

    def test_list_dialetivo_aluno(self):
        self.list_base(self.basenamelist)

    def test_create_dialetivo_aluno(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_dialetivo_aluno(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_dialetivo_aluno(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_dialetivo_aluno(self):
        self.destroy_base(self.instance.id, self.basenamedetail)