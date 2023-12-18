from django.urls import reverse
from rest_framework import status

from pessoas.tests.test_base_pessoas import PessoasTestBase


class PessoasAPITest(PessoasTestBase):
    def test_list_aluno(self):
        url = reverse('pessoas:aluno-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_aluno(self):
        aluno_id = self.aluno.id
        url = reverse('pessoas:aluno-api-detail', args=[aluno_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_aluno(self):
        url = reverse('pessoas:aluno-api-list')
        # data = {
        #     "matricula": "0000000099",
        #     "cpf": "88888888993",
        #     "escola": 1,
        #     "objeto_usuario": {
        #         "first_name": "PrimeiroNomeTeste99",
        #         "last_name": "SobrenomeTeste99",
        #         "email": "email99@teste.com",
        #         "username": "usernameteste99",
        #         "password": "Abcd2341"
        #     }
        # }
        response = self.client.post(url, self.data_create_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_criar_aluno_returns_validation_error(self):
        url = reverse('pessoas:aluno-api-list')
        data = {
            "objeto_usuario": {
                "testando": "email99testecom",
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_aluno(self):
        aluno_id = self.aluno.id
        url = reverse('pessoas:aluno-api-detail', args=[aluno_id])
        data = {
            "matricula": "0000000099",
            "cpf": "88888888993",
            "objeto_usuario": {
                "first_name": "PrimeiroNomeTeste99",
                "last_name": "SobrenomeTeste99",
                "email": "email99@teste.com",
            }
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_aluno(self):
        aluno_id = self.aluno.id
        url = reverse('pessoas:aluno-api-detail', args=[aluno_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_funcionario(self):
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_funcionario(self):
        funcionario_id = self.funcionario.id
        url = reverse('pessoas:funcionario-api-detail', args=[funcionario_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_funcionario(self):
        url = reverse('pessoas:funcionario-api-list')
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
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_funcionario(self):
        funcionario_id = self.funcionario.id
        url = reverse('pessoas:funcionario-api-detail', args=[funcionario_id])
        data = {
            "grupos_add": ["Professores"],
        }
        self.client.patch(url, data, format='json')
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
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_funcionario(self):
        funcionario_id = self.funcionario.id
        url = reverse('pessoas:funcionario-api-detail', args=[funcionario_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)