from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class AlunosAPITest(PessoasAPITestBase):
    def test_list_aluno(self):
        self.list_base('pessoas:aluno-api-list')

    def test_create_aluno(self):
        self.create_base(self.data_create_aluno, 'pessoas:aluno-api-list')

    def test_retrieve_aluno(self):
        self.retrieve_base(self.aluno.id, 'pessoas:aluno-api-detail')

    def test_update_aluno(self):
        data = {
            "matricula": "0000000099",
            "cpf": "88888888993",
            "objeto_usuario": {
                "first_name": "PrimeiroNomeTeste99",
                "last_name": "SobrenomeTeste99",
                "email": "email99@teste.com",
            }
        }
        self.update_base(self.aluno.id, data, 'pessoas:aluno-api-detail')

    def test_destroy_aluno(self):
        self.destroy_base(self.aluno.id, 'pessoas:aluno-api-detail')