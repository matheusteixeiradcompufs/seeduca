from escolas.models import Turma, Sala
from pessoas.models import Boletim, AgendaRecados
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class AgendaRecadosAPITest(PessoasAPITestBase):
    def setUp(self):
        super(AgendaRecadosAPITest, self).setUp()
        turma = Turma.objects.create(
            nome='Teste',
            ano=2023,
            turno='T',
            sala=Sala.objects.create(
                numero=0,
                escola=self.make_escola(
                    cnpj='00000000000002'
                )
            )
        )
        boletim = Boletim.objects.create(
            aluno=self.aluno,
            turma=turma,
        )
        self.agenda = AgendaRecados.objects.get(
            boletim=boletim.id,
        )

    def test_list_agenda_recados(self):
        self.list_base('pessoas:aluno-agenda-api-list')

    def test_retrieve_agenda_recados(self):
        self.retrieve_base(self.agenda.id, 'pessoas:aluno-agenda-api-detail')

    def test_destroy_agenda_recados(self):
        self.destroy_base(self.agenda.id, 'pessoas:aluno-agenda-api-detail')