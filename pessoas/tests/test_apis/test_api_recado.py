from escolas.models import Turma, Sala
from pessoas.models import Boletim, AgendaRecados, Recado
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class RecadoAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        super().setUp()

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
        agenda = AgendaRecados.objects.get(
            boletim=boletim.id,
        )
        texto = "Texto teste"
        self.recado = Recado.objects.create(
            texto=texto,
            agenda=agenda,
        )
        self.data_create_recado = {
            'texto': 'Texto teste 2',
            'agenda': agenda.id,
        }
        self.data_update_recado = {
            'texto': 'Texto teste 3',
        }

    def test_list_recado(self):
        self.list_base('pessoas:aluno-agenda-recado-api-list')

    def test_create_recado(self):
        self.create_base(self.data_create_recado, 'pessoas:aluno-agenda-recado-api-list')

    def test_retrieve_recado(self):
        self.retrieve_base(self.recado.id, 'pessoas:aluno-agenda-recado-api-detail')

    def test_update_recado(self):
        self.update_base(self.recado.id, self.data_update_recado, 'pessoas:aluno-agenda-recado-api-detail')

    def test_destroy_recado(self):
        self.destroy_base(self.recado.id, 'pessoas:aluno-agenda-recado-api-detail')