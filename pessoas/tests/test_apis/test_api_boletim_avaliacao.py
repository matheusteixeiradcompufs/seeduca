from escolas.models import Disciplina, Turma, Sala
from pessoas.models import Avaliacao, Boletim
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class AvaliacaoAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(AvaliacaoAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-boletim-avaliacao-api-list'
        self.basenamedetail = 'pessoas:aluno-boletim-avaliacao-api-detail'

        boletim = Boletim.objects.create(
            ano=2000,
            aluno=self.aluno,
        )
        disciplina = Disciplina.objects.create(
            nome='Teste'
        )
        turma = Turma.objects.create(
            nome='Turma Teste',
            ano=2000,
            turno='manha',
            sala=Sala.objects.create(
                numero=0,
                escola=self.make_escola(
                    cnpj='77777777777777'
                )
            )
        )

        self.data_instance = {
            'nome': 'Teste',
            'aluno': self.aluno,
            'boletim': boletim,
            'disciplina': disciplina,
            'turma': turma,
        }

        self.data_instance2 = {
            'nome': 'Teste 2',
            'aluno': self.aluno.id,
            'boletim': boletim.id,
            'disciplina': disciplina.id,
            'turma': turma.id,
        }

        self.data_instance_update = {
            'ano': 'Atualizado',
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