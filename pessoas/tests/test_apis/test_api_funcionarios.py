from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class FuncionariosAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        self.basenamelist = 'pessoas:funcionario-api-list'
        self.basenamedetail = 'pessoas:funcionario-api-detail'
        return super(FuncionariosAPITest, self).setUp()

    def test_list_funcionario(self):
        self.list_base(self.basenamelist)

    def test_create_funcionario(self):
        funcionario = self.make_usuario(
            first_name="FuncionarioTeste31",
            last_name="SobrenomeTeste31",
            email="teste31@email.com",
            username="funcionarioteste31",
            password="Abcd2341",
            is_superuser=False,
        )
        funcionario.groups.set([self.grupo_coordenadores.id])
        data = {
            "matricula": "0000000031",
            "cpf": "55546595668",
            "usuario": funcionario.id,
        }
        self.create_base(data, self.basenamelist)

    def test_retrieve_funcionario(self):
        self.retrieve_base(self.funcionario.id, self.basenamedetail)

    def test_update_funcionario(self):
        data = {
            "matricula": "0000020032",
            "cpf": "55546595668",
        }
        self.update_base(self.funcionario.id, data, self.basenamedetail)

    def test_destroy_funcionario(self):
        self.destroy_base(self.funcionario.id, self.basenamedetail)