from django.core.exceptions import ValidationError
from django.urls import reverse

from escolas.models import Disciplina, Turma, Sala
from pessoas.models import TelefonePessoa, EmailPessoa, Responsavel, Pessoa, Boletim, Avaliacao, Frequencia, DiaLetivo, \
    Transporte, TelefoneTransporte, AgendaRecados, Recado
from pessoas.tests.test_base_pessoas import PessoasTestBase


class PessoasModelsTestCase(PessoasTestBase):
    def setUp(self) -> None:
        supermodel = super().setUp()
        self.disciplina = Disciplina.objects.create(nome='Test')
        self.turma = Turma.objects.create(
            nome='Teste',
            ano=2024,
            turno='T',
            sala=Sala.objects.create(
                numero=3,
                escola=self.make_escola(
                    cnpj='00000000000003'
                ),
            ),
        )
        self.turma.disciplinas.add(self.disciplina)
        self.boletim = Boletim.objects.create(
            aluno=self.aluno,
            turma=self.turma,
        )
        self.frequencia = Frequencia.objects.get(
            boletim=self.boletim.id,
        )
        self.dialetivo = DiaLetivo.objects.create(
            data='2024-01-01',
            frequencia=self.frequencia
        )
        self.agenda = AgendaRecados.objects.get(
            boletim=self.boletim.id,
        )
        self.avaliacoes = self.boletim.boletim_avaliacoes.all()
        for avaliacao in self.avaliacoes:
            if avaliacao.nome == 'A1':
                avaliacao.nota = 7
                avaliacao.save()
            if avaliacao.nome == 'A2':
                avaliacao.nota = 5
                avaliacao.save()
            if avaliacao.nome == 'R1':
                avaliacao.nota = 10
                avaliacao.save()
            if avaliacao.nome == 'A3':
                avaliacao.nota = 7
                avaliacao.save()
            if avaliacao.nome == 'A4':
                avaliacao.nota = 5
                avaliacao.save()
            if avaliacao.nome == 'R2':
                avaliacao.nota = 8
                avaliacao.save()
        self.a1 = self.avaliacoes.get(nome='A1')
        self.a2 = self.avaliacoes.get(nome='A2')
        self.r1 = self.avaliacoes.get(nome='R1')
        self.a3 = self.avaliacoes.get(nome='A3')
        self.a4 = self.avaliacoes.get(nome='A4')
        self.r2 = self.avaliacoes.get(nome='R2')
        self.situacoes = self.boletim.boletim_situacoes.all()
        return supermodel

    def test_pessoa_model(self):
        pessoa = Pessoa.objects.create(
            matricula='5555555555',
            cpf='55555555555',
            usuario=self.make_usuario(
                first_name='Usuario',
                last_name='Teste',
                username='usuarioteste',
                password='Abcd2341',
                email='email@teste.com',
                is_superuser=True,
            ),
        )
        self.assertEqual(str(pessoa), 'usuarioteste')

    def test_telefone_model(self):
        telefone = TelefonePessoa.objects.create(
            numero='123456789',
            pessoa=self.aluno
        )
        self.assertEqual(str(telefone), '123456789')

    def test_email_model(self):
        email = EmailPessoa.objects.create(
            endereco='test@example.com',
            pessoa=self.aluno
        )
        self.assertEqual(str(email), 'test@example.com')

    def test_aluno_model(self):
        aluno = self.make_aluno(
            matricula='4444444444',
            cpf='44444444444',
            usuario_data={
                'username': 'usuarioteste'
            },
        )
        self.assertEqual(str(aluno), 'usuarioteste')

    def test_responsavel_model(self):
        responsavel = Responsavel.objects.create(
            cpf='98765432101',
            nome='Responsavel Teste',
            observacao='Observacao teste',
            aluno=self.aluno
        )
        self.assertEqual(str(responsavel), 'Responsavel Teste')

    def test_funcionario_model(self):
        funcionario = self.make_funcionario(
            matricula='4444444444',
            cpf='44444444444',
            usuario_data={
                'username': 'usuarioteste'
            },
        )
        self.assertEqual(str(funcionario), 'usuarioteste')

    def test_boletim_model(self):
        self.assertEqual(str(self.boletim), 'Boletim de ' + str(self.aluno.usuario.first_name) + ' da turma ' + str(self.turma))

    def test_avaliacao_model(self):
        self.assertEqual(str(self.a1), f'1ª Avaliação - {self.disciplina.nome}')

    def test_create_avaliacao_model(self):
        avaliacao = Avaliacao.objects.create(
            nome="A1",
            aluno=self.aluno,
            disciplina=self.disciplina,
            boletim=self.boletim,
        )
        self.assertEqual(str(avaliacao), f'{avaliacao.get_nome_display()} - {self.disciplina.nome}')

    def test_if_m1_returns_validation_error_if_a2_confirmar_is_true_before_a1_confirmar(self):
        with self.assertRaises(ValidationError) as context:
            for avaliacao in self.avaliacoes:
                if avaliacao.nome == 'A2':
                    avaliacao.confirmar = True
                    avaliacao.save()
        self.assertEqual(
            context.exception.message,
            "Existem avaliações dessa matéria pendentes de confirmação no 1º semestre"
        )

    def test_if_m1_receive_a1_if_confirmar_is_true(self):
        for avaliacao in self.avaliacoes:
            if avaliacao.nome == 'A1':
                avaliacao.confirmar = True
                avaliacao.save()
        medias = self.boletim.boletim_medias.all()
        m1 = medias.get(tipo='M1')
        self.assertEqual(self.a1.nota, m1.valor)

    def test_if_m1_receive_media_of_a1_and_a2_if_confirmar_is_true(self):
        for avaliacao in self.avaliacoes:
            if avaliacao.nome == 'A1':
                avaliacao.confirmar = True
                avaliacao.save()
            if avaliacao.nome == 'A2':
                avaliacao.confirmar = True
                avaliacao.save()
        medias = self.boletim.boletim_medias.all()
        m1 = medias.get(tipo='M1')
        self.assertEqual((self.a1.nota + self.a2.nota) / 2, m1.valor)

    def test_if_m1_receive_media_of_m1_and_r1_if_confirmar_is_true(self):
        for avaliacao in self.avaliacoes:
            if avaliacao.nome == 'A1':
                avaliacao.confirmar = True
                avaliacao.save()
            if avaliacao.nome == 'A2':
                avaliacao.confirmar = True
                avaliacao.save()
            if avaliacao.nome == 'R1':
                avaliacao.confirmar = True
                avaliacao.save()
        medias = self.boletim.boletim_medias.all()
        m1 = medias.get(tipo='M1')
        self.assertEqual(((self.a1.nota + self.a2.nota) / 2 + self.r1.nota) / 2, m1.valor)

    def test_if_m1_receive_media_of_m1_and_if_r1_less_then_m1_if_confirmar_is_true(self):
        for avaliacao in self.avaliacoes:
            if avaliacao.nome == 'A1':
                avaliacao.confirmar = True
                avaliacao.save()
            if avaliacao.nome == 'A2':
                avaliacao.confirmar = True
                avaliacao.save()
            if avaliacao.nome == 'R1':
                avaliacao.nota = 3
                avaliacao.confirmar = True
                avaliacao.save()
        medias = self.boletim.boletim_medias.all()
        m1 = medias.get(tipo='M1')
        self.assertEqual((self.a1.nota + self.a2.nota) / 2, m1.valor)

    def test_if_m2_returns_validation_error_if_a4_confirmar_is_true_before_a3_confirmar(self):
        with self.assertRaises(ValidationError) as context:
            for avaliacao in self.avaliacoes:
                if avaliacao.nome == 'A4':
                    avaliacao.confirmar = True
                    avaliacao.save()
        self.assertEqual(
            context.exception.message,
            "Existem avaliações dessa matéria pendentes de confirmação no 2º semestre"
        )

    def test_if_m2_receive_a3_if_confirmar_is_true(self):
        for avaliacao in self.avaliacoes:
            if avaliacao.nome == 'A3':
                avaliacao.confirmar = True
                avaliacao.save()
        medias = self.boletim.boletim_medias.all()
        m2 = medias.get(tipo='M2')
        self.assertEqual(self.a3.nota, m2.valor)

    def test_if_m2_receive_media_of_a3_and_a4_if_confirmar_is_true(self):
        for avaliacao in self.avaliacoes:
            if avaliacao.nome == 'A3':
                avaliacao.confirmar = True
                avaliacao.save()
            if avaliacao.nome == 'A4':
                avaliacao.confirmar = True
                avaliacao.save()
        medias = self.boletim.boletim_medias.all()
        m2 = medias.get(tipo='M2')
        self.assertEqual((self.a3.nota + self.a4.nota) / 2, m2.valor)

    def test_if_m2_receive_media_of_m2_and_r2_if_confirmar_is_true(self):
        for avaliacao in self.avaliacoes:
            if avaliacao.nome == 'A3':
                avaliacao.confirmar = True
                avaliacao.save()
            if avaliacao.nome == 'A4':
                avaliacao.confirmar = True
                avaliacao.save()
            if avaliacao.nome == 'R2':
                avaliacao.confirmar = True
                avaliacao.save()
        medias = self.boletim.boletim_medias.all()
        m2 = medias.get(tipo='M2')
        self.assertEqual(((self.a3.nota + self.a4.nota) / 2 + self.r2.nota) / 2, m2.valor)

    def test_if_m2_receive_media_of_m2_and_if_r2_less_then_m2_if_confirmar_is_true(self):
        for avaliacao in self.avaliacoes:
            if avaliacao.nome == 'A3':
                avaliacao.confirmar = True
                avaliacao.save()
            if avaliacao.nome == 'A4':
                avaliacao.confirmar = True
                avaliacao.save()
            if avaliacao.nome == 'R2':
                avaliacao.nota = 3
                avaliacao.confirmar = True
                avaliacao.save()
        medias = self.boletim.boletim_medias.all()
        m2 = medias.get(tipo='M2')
        self.assertEqual((self.a3.nota + self.a4.nota) / 2, m2.valor)

    def test_situacao_model(self):
        situacao = self.situacoes.get(disciplina=self.disciplina)
        self.assertEqual(str(situacao), f'Situação de {self.disciplina}')

    def test_if_situacao_returns_A_if_finalizar_true_and_mg_more_than_5(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 6
            avaliacao.confirmar = True
            avaliacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = True
            situacao.save()
        self.assertEqual(situacao.situacao, 'A')

    def test_if_boletim_status_returns_A(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 6
            avaliacao.confirmar = True
            avaliacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = True
            situacao.save()
        self.boletim.encerrar = True
        self.boletim.save()
        boletim = Boletim.objects.all().get(pk=self.boletim.id)
        boletim.save()
        self.assertEqual(boletim.status, 'A')

    def test_if_boletim_status_returns_RM(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 4
            avaliacao.confirmar = True
            avaliacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = True
            situacao.save()
        self.boletim.encerrar = True
        self.boletim.save()
        boletim = Boletim.objects.all().get(pk=self.boletim.id)
        boletim.save()
        self.assertEqual(boletim.status, 'RM')

    def test_if_boletim_status_returns_RF(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 6
            avaliacao.confirmar = True
            avaliacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = True
            situacao.save()
        self.dialetivo.presenca = False
        self.dialetivo.save()
        self.boletim.encerrar = True
        self.boletim.save()
        boletim = Boletim.objects.all().get(pk=self.boletim.id)
        boletim.save()
        self.assertEqual(boletim.status, 'RF')

    def test_if_boletim_status_returns_RFM(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 4
            avaliacao.confirmar = True
            avaliacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = True
            situacao.save()
        self.dialetivo.presenca = False
        self.dialetivo.save()
        self.boletim.encerrar = True
        self.boletim.save()
        boletim = Boletim.objects.all().get(pk=self.boletim.id)
        boletim.save()
        self.assertEqual(boletim.status, 'RFM')

    def test_if_situacao_returns_A_if_finalizar_true_and_mg_less_than_5(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 4
            avaliacao.confirmar = True
            avaliacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = True
            situacao.save()
        self.assertEqual(situacao.situacao, 'R')

    def test_if_avaliacao_returns_raise_if_finalizar_is_true(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 4
            avaliacao.confirmar = True
            avaliacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = True
            situacao.save()
        with self.assertRaises(ValidationError) as context:
            for avaliacao in self.avaliacoes:
                avaliacao.nota = 5
                avaliacao.confirmar = True
                avaliacao.save()
        self.assertEqual(
            context.exception.message,
            'As notas de uma matéria finalizada não podem mais ser editadas!'
        )

    def test_if_avaliacao_returns_raise_if_boletim_encerrar_is_true(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 4
            avaliacao.confirmar = True
            avaliacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = True
            situacao.save()
        self.boletim.encerrar = True
        self.boletim.save()
        with self.assertRaises(ValidationError) as context:
            for avaliacao in self.avaliacoes:
                avaliacao.nota = 5
                avaliacao.confirmar = True
                avaliacao.save()
        self.assertEqual(
            context.exception.message,
            'Os boletins encerrados não podem mais ser editados!'
        )

    def test_if_boletim_returns_raise_if_some_situacao_finalizar_is_false(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 4
            avaliacao.confirmar = True
            avaliacao.save()
        with self.assertRaises(ValidationError) as context:
            self.boletim.encerrar = True
            self.boletim.save()
        self.assertEqual(
            context.exception.message,
            'Alguma matéria ainda não foi finalizada!'
        )

    def test_if_situacao_finalizar_set_mg_to_0_if_value_equals_false(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 4
            avaliacao.confirmar = True
            avaliacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = True
            situacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = False
            situacao.save()
        medias = self.boletim.boletim_medias.all()
        mg = medias.get(tipo='MG')
        self.assertEqual(0, mg.valor)

    def test_if_boletim_raises_if_encerrar_equals_true_and_try_edit_boletim(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 4
            avaliacao.confirmar = True
            avaliacao.save()
        for situacao in self.situacoes:
            situacao.finalizar = True
            situacao.save()
        self.boletim.encerrar = True
        self.boletim.save()
        with self.assertRaises(ValidationError) as context:
            for situacao in self.situacoes:
                situacao.finalizar = False
                situacao.save()
        self.assertEqual(
            context.exception.message,
            'Os boletins encerrados não podem mais ser editados!'
        )

    def test_if_situacao_raises_validation_error_if_some_avaliacao_confirmar_is_false(self):
        for avaliacao in self.avaliacoes:
            avaliacao.nota = 6
            avaliacao.confirmar = True
            avaliacao.save()
        r2 = self.avaliacoes.get(nome='R2')
        r2.confirmar = False
        r2.save()
        with self.assertRaises(ValidationError) as context:
            for situacao in self.situacoes:
                situacao.finalizar = True
                situacao.save()
        self.assertEqual(
            context.exception.message,
            'Só é possível finalizar uma matéria quando todas as notas do ano forem confirmadas'
        )

    def test_frequencia_model(self):
        self.assertEqual(str(self.frequencia), f'Frequência de {self.boletim.aluno} em {self.boletim.turma.ano} da turma {self.boletim.turma}')

    def test_frequencia_dialetivo_model(self):
        self.assertEqual(str(self.dialetivo), '2024-01-01')

    def test_transporte_model(self):
        transporte = Transporte.objects.create(
            placa='BBB0000',
            ano=2023
        )
        self.assertEqual(str(transporte), 'BBB0000')

    def test_transporte_telefone_model(self):
        telefone = TelefoneTransporte.objects.create(
            numero='11111111111',
            transporte=Transporte.objects.create(
                placa='BBB0000',
                ano=2023
            )
        )
        self.assertEqual(str(telefone), '11111111111')

    def test_agenda_recados_model(self):
        self.assertEqual(str(self.agenda), f'Agenda de Recados de {self.boletim.turma.ano}')

    def test_recados_model(self):
        self.make_authenticate(self.aluno.usuario)
        data = {
            "texto": "Texto teste",
            "agenda": self.agenda.id,
        }
        url = reverse('pessoas:aluno-agenda-recado-api-list')
        response = self.client.post(url, data, format='json')
        recado = Recado.objects.get(pk=response.data["id"])
        self.assertEqual(str(recado), f'Recado de {recado.pessoa} em {recado.publicado_em}')
