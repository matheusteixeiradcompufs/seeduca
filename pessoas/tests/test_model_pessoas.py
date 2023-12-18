from pessoas.models import Telefone, Email, EhPCD, Responsavel
from pessoas.tests.test_base_pessoas import PessoasTestBase


class PessoasModelsTestCase(PessoasTestBase):
    def test_pessoa_model(self):
        pessoa = self.aluno
        self.assertEqual(str(pessoa), str(pessoa.usuario))

    def test_telefone_model(self):
        telefone = Telefone.objects.create(numero='123456789', pessoa=self.aluno)
        self.assertEqual(str(telefone), '123456789')

    def test_email_model(self):
        email = Email.objects.create(endereco='test@example.com', pessoa=self.aluno)
        self.assertEqual(str(email), 'test@example.com')

    def test_aluno_model(self):
        self.assertEqual(str(self.aluno), str(self.aluno.usuario))

    def test_ehpcd_model(self):
        ehpcd = EhPCD.objects.create(eh_pcd=True, descricao='Teste PCD', aluno=self.aluno)
        self.assertEqual(str(ehpcd), 'True')

    def test_responsavel_model(self):
        responsavel = Responsavel.objects.create(cpf='98765432101', nome='Responsavel Teste', observacao='Observacao teste', aluno=self.aluno)
        self.assertEqual(str(responsavel), 'Responsavel Teste')

    def test_funcionario_model(self):
        self.assertEqual(str(self.funcionario), str(self.funcionario.usuario))