from escolas.models import Tarefa, DiaAgenda, AgendaEscolar, Turma, Sala
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class TarefaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(TarefaAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-sala-turma-agenda-dia-tarefa-api-list'
        self.basenamedetail = 'escolas:escola-sala-turma-agenda-dia-tarefa-api-detail'

        self.data_instance = {
            'nome': 'Teste',
            'descricao': 'Descrição Teste',
            'tipo': 'E',
            'diaAgenda': DiaAgenda.objects.create(
                data='2000-01-02',
                agenda=AgendaEscolar.objects.create(
                    turma=Turma.objects.create(
                        nome='Teste1',
                        ano=2001,
                        turno='Teste1',
                        sala=Sala.objects.create(
                            numero=2,
                            escola=self.escola
                        ),
                    )
                )
            )
        }

        self.data_instance2 = {
            'nome': 'Teste',
            'descricao': 'Descrição Teste',
            'tipo': 'E',
            'diaAgenda': DiaAgenda.objects.create(
                data='2000-01-03',
                agenda=AgendaEscolar.objects.create(
                    turma=Turma.objects.create(
                        nome='Teste2',
                        ano=2001,
                        turno='Teste1',
                        sala=Sala.objects.create(
                            numero=3,
                            escola=self.escola
                        ),
                    )
                )
            ).id
        }

        self.data_instance_update = {
            'descricao': 'Texto atualizado',
        }

        self.instance = Tarefa.objects.create(**self.data_instance)
        return supersetup

    def test_list_tarefa(self):
        self.list_base(self.basenamelist)

    def test_create_tarefa(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_tarefa(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_tarefa(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_tarefa(self):
        self.destroy_base(self.instance.id, self.basenamedetail)
