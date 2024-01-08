from escolas.models import Disciplina, Turma, Sala
from pessoas.models import TelefonePessoa, EmailPessoa, Responsavel, Pessoa, Boletim, Avaliacao, Frequencia, DiaLetivo, \
    Transporte, TelefoneTransporte
from pessoas.tests.test_base_pessoas import PessoasTestBase


class PessoasModelsTestCase(PessoasTestBase):
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
            escola=self.make_escola(
                cnpj='55555555555555',
                nome='Escola Teste',
                endereco='Endereco Teste',
            )
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
            escola_data={
                'cnpj': '23232323232323'
            }
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
            escola_data={
                'cnpj': '23232323232323'
            }
        )
        self.assertEqual(str(funcionario), 'usuarioteste')

    def test_boletim_model(self):
        turma = Turma.objects.create(
            nome='Teste',
            ano=2023,
            turno='teste',
            sala=Sala.objects.create(
                numero=0,
                escola=self.make_escola(
                    cnpj='00000000000002'
                )
            )
        )
        self.aluno.turmas.add(turma)
        boletim = Boletim.objects.create(
            ano=2023,
            aluno=self.aluno,
        )
        self.assertEqual(str(boletim), 'Boletim de ' + str(self.aluno.usuario.first_name) + ' em ' + str(2023))

    def test_avaliacao_model(self):
        turma = Turma.objects.create(
            nome='Teste',
            ano=2023,
            turno='teste',
            sala=Sala.objects.create(
                numero=0,
                escola=self.make_escola(
                    cnpj='00000000000002'
                )
            )
        )
        self.aluno.turmas.add(turma)
        avaliacao = Avaliacao.objects.create(
            nome='Avaliacao Teste',
            aluno=self.aluno,
            disciplina=Disciplina.objects.create(
                nome='Teste'
            ),
            boletim=Boletim.objects.create(
                ano=2023,
                aluno=self.aluno,
            ),
            turma=turma
        )
        self.assertEqual(str(avaliacao), 'Avaliacao Teste')

    def test_frequencia_model(self):
        frequencia = Frequencia.objects.create(
            ano=2000,
            aluno=self.aluno,
        )
        self.assertEqual(str(frequencia), 'Frequência de ' + self.aluno.usuario.first_name + 'em ' + str(2000))

    def test_frequencia_dialetivo_model(self):
        dialetivo = DiaLetivo.objects.create(
            data='2000-01-01',
            frequencia=Frequencia.objects.create(
                ano=2000,
                aluno=self.aluno,
            )
        )
        self.assertEqual(str(dialetivo), '2000-01-01')

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