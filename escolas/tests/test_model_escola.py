from escolas.models import Telefone, Email
from escolas.tests.test_base_escola import EscolaTestBase


class EscolaModelTestCase(EscolaTestBase):
    def test_if_instace_escola_returns_name_in_str(self):
        nome = 'Nome Teste Escola'
        escola = self.make_escola(cnpj='00000000000001', nome=nome)
        self.assertEqual(escola.__str__(), nome)

    def test_if_instace_telefone_returns_numero_in_str(self):
        numero = '99999999999'
        telefone = Telefone.objects.create(numero=numero)
        self.assertEqual(telefone.__str__(), numero)

    def test_if_instace_email_returns_endereco_in_str(self):
        endereco = 'teste@teste.com'
        email = Email.objects.create(endereco=endereco)
        self.assertEqual(email.__str__(), endereco)