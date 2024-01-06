from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class FuncionariosAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        self.basenamelist = 'pessoas:funcionario-api-list'
        self.basenamedetail = 'pessoas:funcionario-api-detail'
        return super(FuncionariosAPITest, self).setUp()

    def test_list_funcionario(self):
        self.list_base(self.basenamelist)

    def test_create_funcionario(self):
        data = {
            "matricula": "0000000031",
            "cpf": "55546595668",
            "escola": 1,
            "grupos_add": ["Coordenadores"],
            "objeto_usuario": {
                "first_name": "FuncionarioTeste31",
                "last_name": "SobrenomeTeste31",
                "email": "teste31@email.com",
                "username": "funcionarioteste31",
                "password": "Abcd2341"
            }
        }
        self.create_base(data, self.basenamelist)

    def test_retrieve_funcionario(self):
        self.retrieve_base(self.funcionario.id, self.basenamedetail)

    def test_update_funcionario(self):
        data = {
            "matricula": "0000000031",
            "cpf": "55546595668",
            "grupos_remove": ["Professores"],
            "grupos_add": ["Coordenadores"],
            "objeto_usuario": {
                "first_name": "FuncionarioTeste31",
                "last_name": "SobrenomeTeste31",
                "email": "teste31@email.com",
            }
        }
        self.update_base(self.funcionario.id, data, self.basenamedetail)

    def test_destroy_funcionario(self):
        self.destroy_base(self.funcionario.id, self.basenamedetail)