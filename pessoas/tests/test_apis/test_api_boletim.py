from escolas.models import Turma, Sala
from pessoas.models import Boletim
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class BoletimAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(BoletimAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-boletim-api-list'
        self.basenamedetail = 'pessoas:aluno-boletim-api-detail'

        escola = self.make_escola(
            cnpj='00000000000002'
        )
        sala = Sala.objects.create(
            numero=0,
            escola=escola
        )

        turma = Turma.objects.create(
            nome='Teste1',
            ano=2023,
            turno='T',
            sala=sala
        )

        self.data_instance = {
            'turma': turma,
            'aluno': self.aluno,
        }

        turma = Turma.objects.create(
            nome='Teste2',
            ano=2024,
            turno='T',
            sala=sala
        )

        self.data_instance2 = {
            'turma': turma.id,
            'aluno': self.aluno.id,
        }

        self.data_instance_update = {
            'turma': turma.id,
        }

        self.instance = Boletim.objects.create(**self.data_instance)
        return supersetup

    def test_list_boletim_aluno(self):
        self.list_base(self.basenamelist)

    def test_create_boletim_aluno(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_boletim_aluno(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_boletim_aluno(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_boletim_aluno(self):
        self.destroy_base(self.instance.id, self.basenamedetail)