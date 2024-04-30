from escolas.models import Disciplina, Turma, Sala
from pessoas.models import Frequencia, Boletim
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class FrequenciaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(FrequenciaAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-frequencia-api-list'
        self.basenamedetail = 'pessoas:aluno-frequencia-api-detail'

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
            ano=2000,
            turno='M',
            sala=sala
        )
        turma.disciplinas.add(disciplina)
        self.boletim = Boletim.objects.create(
            turma=turma,
            aluno=self.aluno,
        )

        self.data_instance = {
            'boletim': self.boletim,
        }

        turma2 = Turma.objects.create(
            nome='Turma Teste2',
            ano=2024,
            turno='T',
            sala=sala
        )
        turma2.disciplinas.add(disciplina)
        self.boletim2 = Boletim.objects.create(
            turma=turma2,
            aluno=self.aluno,
        )
        self.data_instance2 = {
            'boletim': self.boletim2,
        }

        self.data_instance_update = {
            'turma': turma2.id,
        }

        self.instance = self.boletim.boletim_frequencia
        return supersetup

    def test_list_frequencia_aluno(self):
        self.list_base(self.basenamelist)

    def test_if_frequencia_was_created(self):
        self.assertEqual(
            str(self.boletim.boletim_frequencia),
            f'Frequência de {self.boletim.aluno} em {self.boletim.turma.ano} da turma {self.boletim.turma}'
        )

    def test_retrieve_frequencia_aluno(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_frequencia_aluno(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_frequencia_aluno(self):
        self.destroy_base(self.instance.id, self.basenamedetail)