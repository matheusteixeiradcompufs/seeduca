from django.urls import reverse
from rest_framework import status

from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class ResetPasswordAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        super(ResetPasswordAPITest, self).setUp()

    def test_if_reset_password_returns_200(self):
        data = {
            "email": self.aluno.usuario.email
        }
        url = reverse("pessoas:reset_password_request")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_reset_password_returns_404(self):
        data = {
            "email": "naoexiste@email.com"
        }
        url = reverse("pessoas:reset_password_request")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)