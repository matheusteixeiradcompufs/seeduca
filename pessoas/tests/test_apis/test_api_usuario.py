from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class UsuarioAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        self.basenamelist = 'pessoas:usuario-api-list'
        self.basenamedetail = 'pessoas:usuario-api-detail'
        return super(UsuarioAPITest, self).setUp()

    def test_list_usuario(self):
        self.list_base(self.basenamelist)

    def test_create_usuario(self):
        data = {
            "first_name": "Usuario",
            "last_name": "Teste",
            "email": "usuarioteste@gmail.com",
            "username": "usuario.teste",
            "password": "Abcd2341",
            "is_superuser": False
        }
        self.create_base(data, self.basenamelist)

    def test_retrieve_usuario(self):
        self.retrieve_base(self.usuario.id, self.basenamedetail)

    def test_update_usuario(self):
        data = {
            "password": "Abcd2341",
        }
        self.update_base(self.usuario.id, data, self.basenamedetail)
        data = {
            "first_name": "Usuario1",
        }
        self.update_base(self.usuario.id, data, self.basenamedetail)

    def test_destroy_usuario(self):
        self.destroy_base(self.usuario.id, self.basenamedetail)