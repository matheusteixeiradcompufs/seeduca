from django.urls import reverse
from rest_framework import status

from pessoas.tests.test_base_pessoas import PessoasTestBase


class SerializerPessoaTest(PessoasTestBase):
    def setUp(self) -> None:
        return super(SerializerPessoaTest, self).setUp()

    def test_if_create_usuario_returns_bad_request(self):
        url = reverse('pessoas:aluno-api-list')
        data = {
            "matricula": "1000000001",
            "cpf": "10000000001",
            "escola": self.escola.id,
            "objeto_usuario": {
                "first_name": "PrimeiroNome",
                "last_name": "Sobrenome",
                "username": "username11",
                "password": "Abcd2341",
                "email": "emailteste.com"
            }
        }
        response = self.client.post(
            url,
            data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_update_usuario_returns_bad_request(self):
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        data = {
            "objeto_usuario": {
                "email": "emailteste.com"
            }
        }
        response = self.client.patch(
            url,
            data,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)