from escolas.models import Disciplina, Turma, Sala
from pessoas.models import Avaliacao, Boletim
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class AvaliacaoAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(AvaliacaoAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-boletim-avaliacao-api-list'
        self.basenamedetail = 'pessoas:aluno-boletim-avaliacao-api-detail'

        disciplina = Disciplina.objects.create(
            nome='Teste'
        )
        turma = Turma.objects.create(
            nome='Turma Teste',
            ano=2000,
            turno='M',
            sala=Sala.objects.create(
                numero=0,
                escola=self.make_escola(
                    cnpj='77777777777777'
                )
            )
        )
        turma.disciplinas.add(disciplina)
        boletim = Boletim.objects.create(
            turma=turma,
            aluno=self.aluno,
        )

        self.data_instance = {
            'nome': 'A1',
            'aluno': self.aluno,
            'boletim': boletim,
            'disciplina': disciplina,
        }

        self.data_instance2 = {
            'nome': 'A2',
            'aluno': self.aluno.id,
            'boletim': boletim.id,
            'disciplina': disciplina.id,
        }
        self.data_instance_update = {
            'disciplina': disciplina.id,
        }

        self.instance = Avaliacao.objects.create(**self.data_instance)
        return supersetup

    def test_list_avaliacao_aluno(self):
        self.list_base(self.basenamelist)

    def test_create_avaliacao_aluno(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_avaliacao_aluno(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_avaliacao_aluno(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_avaliacao_aluno(self):
        self.destroy_base(self.instance.id, self.basenamedetail)