from django.urls import reverse
from rest_framework import status

from escolas.models import Sala, Turma
from pessoas.models import Boletim
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class DecodeTokenAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        super(DecodeTokenAPITest, self).setUp()
        self.boletim = Boletim.objects.create(
            aluno=self.aluno,
            turma=Turma.objects.create(
                nome='Teste',
                ano=2023,
                turno='T',
                sala=Sala.objects.create(
                    numero=0,
                    escola=self.make_escola(
                        cnpj='00000000000002'
                    )
                )
            ),
        )

    def test_if_decode_token_returns_200(self):
        data = {
            "token": self.boletim.token
        }
        url = reverse("pessoas:decode_token")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_decode_token_returns_400_no_token(self):
        data = {}
        url = reverse("pessoas:decode_token")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.data["error"], 'Parâmetro "token" não encontrado na requisição')

    def test_if_decode_token_returns_400_invalid_token(self):
        data = {
            "token": 'self.boletim.token'
        }
        url = reverse("pessoas:decode_token")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.data["error"], 'Token inválido')