from escolas.models import Aviso, DiaAgenda, AgendaEscolar, Turma, Sala
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class AvisoAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(AvisoAPITest, self).setUp()

        self.basenamelist = 'escolas:escola-sala-turma-agenda-dia-aviso-api-list'
        self.basenamedetail = 'escolas:escola-sala-turma-agenda-dia-aviso-api-detail'

        self.data_instance = {
            'titulo': 'Teste',
            'texto': 'Texto Teste',
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
            'titulo': 'Teste',
            'texto': 'Texto Teste',
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
            'texto': 'Texto atualizado',
        }

        self.instance = Aviso.objects.create(**self.data_instance)
        return supersetup

    def test_list_aviso(self):
        self.list_base(self.basenamelist)

    def test_create_aviso(self):
        self.create_base(self.data_instance2, self.basenamelist)

    def test_retrieve_aviso(self):
        self.retrieve_base(self.instance.id, self.basenamedetail)

    def test_update_aviso(self):
        self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)

    def test_destroy_aviso(self):
        self.destroy_base(self.instance.id, self.basenamedetail)