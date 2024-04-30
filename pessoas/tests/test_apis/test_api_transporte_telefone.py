from pessoas.models import TelefoneTransporte, Transporte
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class TelefoneTransporteAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(TelefoneTransporteAPITest, self).setUp()

        self.basenamelist = 'pessoas:transporte-telefone-api-list'
        self.basenamedetail = 'pessoas:transporte-telefone-api-detail'

        transporte = Transporte.objects.create(
            placa='CCC0000',
            ano=2000,
            tipo='X',
        )

        self.data_instance = {
            'numero': '88888888888',
            'transporte': transporte,
        }

        self.data_instance2 = {
            'numero': '88888888889',
            'transporte': transporte.id,
        }

        self.data_instance_update = {
            'numero': '88888888899',
        }

        self.instance = TelefoneTransporte.objects.create(**self.data_instance)
        return supersetup

    def test_list_transporte_telefone_aluno(self):
        self.list_base(self.basenamelist)

    def test_create_transporte_telefone_aluno(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_transporte_telefone_aluno(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_transporte_telefone_aluno(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_transporte_telefone_aluno(self):
        self.destroy_base(self.instance.id, self.basenamedetail)