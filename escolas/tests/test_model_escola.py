from escolas.models import TelefoneEscola, EmailEscola, Disciplina, Sala, Turma, AgendaEscolar, DiaAgenda, Aviso, \
    Tarefa, ItemCardapioMerenda, CardapioMerenda, Email, Telefone
from escolas.tests.test_base_escola import EscolaTestBase


class EscolaModelTestCase(EscolaTestBase):
    def test_if_instace_escola_returns_name_in_str(self):
        nome = 'Nome Teste Escola'
        escola = self.make_escola(
            cnpj='00000000000001',
            nome=nome
        )
        self.assertEqual(str(escola), nome)

    def test_if_instace_telefone_returns_numero_in_str(self):
        numero = '99999999999'
        telefone = Telefone.objects.create(
            numero=numero,
        )
        self.assertEqual(str(telefone), numero)

    def test_if_instace_email_returns_endereco_in_str(self):
        endereco = 'teste@teste.com'
        email = Email.objects.create(
            endereco=endereco,
        )
        self.assertEqual(str(email), endereco)

    def test_if_instace_telefone_escola_returns_numero_in_str(self):
        numero = '99999999999'
        telefone = TelefoneEscola.objects.create(
            numero=numero,
            escola=self.escola,
        )
        self.assertEqual(str(telefone), numero)

    def test_if_instace_email_escola_returns_endereco_in_str(self):
        endereco = 'teste@teste.com'
        email = EmailEscola.objects.create(
            endereco=endereco,
            escola=self.escola,
        )
        self.assertEqual(str(email), endereco)

    def test_if_instace_disciplina_returns_nome_in_str(self):
        nome = 'Teste'
        disciplina = Disciplina.objects.create(
            nome=nome
        )
        self.assertEqual(str(disciplina), nome)

    def test_if_instace_sala_returns_formated_numero_in_str(self):
        numero = 0
        sala = Sala.objects.create(
            numero=numero,
            escola=self.escola,
        )
        self.assertEqual(str(sala), '000')

    def test_if_instance_turma_returns_nome_in_str(self):
        nome = 'Turma Teste'
        ano = 2000
        turno = 'Teste'
        sala = Sala.objects.create(
            numero=0,
            escola=self.escola,
        )
        turma = Turma.objects.create(
            nome=nome,
            ano=ano,
            turno=turno,
            sala=sala
        )
        self.assertEqual(str(turma), nome)

    def test_if_instance_agenda_escolar_returns_turma_in_str(self):
        nome = 'Turma Teste'
        ano = 2000
        turno = 'Teste'
        sala = Sala.objects.create(
            numero=0,
            escola=self.escola,
        )
        turma = Turma.objects.create(
            nome=nome,
            ano=ano,
            turno=turno,
            sala=sala
        )
        agenda = AgendaEscolar.objects.create(
            turma=turma
        )
        self.assertEqual(str(agenda), 'Agenda do Turma Teste')

    def test_if_instance_dia_agenda_escolar_returns_data_in_str(self):
        nome = 'Turma Teste'
        ano = 2000
        turno = 'Teste'
        sala = Sala.objects.create(
            numero=0,
            escola=self.escola,
        )
        turma = Turma.objects.create(
            nome=nome,
            ano=ano,
            turno=turno,
            sala=sala
        )
        agenda = AgendaEscolar.objects.create(
            turma=turma
        )
        dia = DiaAgenda.objects.create(
            data='2000-01-01',
            agenda=agenda,
        )
        self.assertEqual(str(dia), '2000-01-01')

    def test_if_instance_aviso_returns_titulo_in_str(self):
        nome = 'Turma Teste'
        ano = 2000
        turno = 'Teste'
        sala = Sala.objects.create(
            numero=0,
            escola=self.escola,
        )
        turma = Turma.objects.create(
            nome=nome,
            ano=ano,
            turno=turno,
            sala=sala
        )
        agenda = AgendaEscolar.objects.create(
            turma=turma
        )
        dia = DiaAgenda.objects.create(
            data='2000-01-01',
            agenda=agenda,
        )
        aviso = Aviso.objects.create(
            titulo='Teste',
            texto='Texto Teste',
            diaAgenda=dia,
        )
        self.assertEqual(str(aviso), 'Teste')

    def test_if_instance_tarefa_returns_nome_in_str(self):
        nome = 'Turma Teste'
        ano = 2000
        turno = 'Teste'
        sala = Sala.objects.create(
            numero=0,
            escola=self.escola,
        )
        turma = Turma.objects.create(
            nome=nome,
            ano=ano,
            turno=turno,
            sala=sala
        )
        agenda = AgendaEscolar.objects.create(
            turma=turma
        )
        dia = DiaAgenda.objects.create(
            data='2000-01-01',
            agenda=agenda,
        )
        tarefa = Tarefa.objects.create(
            nome='Teste',
            descricao='Texto Teste',
            diaAgenda=dia,
        )
        self.assertEqual(str(tarefa), 'Teste')

    def test_if_instance_item_cardapio_returns_nome_in_str(self):
        nome = 'Item Teste'
        descricao = 'Descricao Teste'
        item = ItemCardapioMerenda.objects.create(
            nome=nome,
            descricao=descricao,
        )
        self.assertEqual(str(item), nome)

    def test_if_instance_cardapio_returns_data_and_turno_in_str(self):
        data = '2000-01-01'
        turno = 'teste'
        cardapio = CardapioMerenda.objects.create(
            data=data,
            turno=turno,
            escola=self.escola,
        )
        self.assertEqual(str(cardapio), 'Cardápio de 2000-01-01 do turno teste')