from escolas.models import Disciplina, Sala, Turma
from pessoas.models import DiaLetivo, Frequencia, Boletim
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class DiaLetivoAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(DiaLetivoAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-frequencia-dialetivo-api-list'
        self.basenamedetail = 'pessoas:aluno-frequencia-dialetivo-api-detail'

        disciplina = Disciplina.objects.create(
            nome='Teste'
        )
        sala = Sala.objects.create(
            numero=0,
            escola=self.make_escola(
                cnpj='77777777777777'
            )
        )
        turma = Turma.objects.create(
            nome='Turma Teste',
            ano=2023,
            turno='M',
            sala=sala
        )
        turma.disciplinas.add(disciplina)
        boletim = Boletim.objects.create(
            turma=turma,
            aluno=self.aluno,
        )
        frequencia = boletim.boletim_frequencia

        self.data_instance = {
            'data': '2023-12-29',
            'frequencia': frequencia,
        }

        self.data_instance2 = {
            'data': '2023-12-30',
            'frequencia': frequencia.id,
        }

        self.data_instance_update = {
            'ano': '2023-12-31',
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