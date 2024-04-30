from django.urls import reverse
from rest_framework import status

from pessoas.models import Responsavel
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class GetMeAlunoAPITest(PessoasAPITestBase):
    def logar_aluno(self):
        self.make_authenticate(self.aluno)

    def logar_professor(self):
        self.make_authenticate(self.funcionario)
        self.funcionario.usuario.groups.add(self.grupo_professores)

    def setUp(self) -> None:
        supersetup = super(GetMeAlunoAPITest, self).setUp()

        self.get_me_aluno = 'pessoas:get_me_aluno'

        self.data = {
            'username': self.aluno.usuario.username,
        }

        self.data2 = {
            'user': self.funcionario.usuario.username,
        }

        self.data3 = {
            'username': self.aluno.usuario.username,
        }

        return supersetup

    def test_if_get_me_aluno_returns_bad_request(self):
        self.logar_aluno()
        url = reverse(self.get_me_aluno)
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_if_get_me_returns_forbidden(self):
        self.logar_professor()
        url = reverse(self.get_me_aluno)
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_get_me_returns_not_found(self):
        self.logar_aluno()
        url = reverse(self.get_me_aluno)
        response = self.client.post(url, {'username': 'teste'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_get_me_returns_OK(self):
        self.logar_aluno()
        url = reverse(self.get_me_aluno)
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_get_me_returns_forbidden_if_superuser(self):
        self.logar_aluno()
        self.aluno.usuario.is_superuser = True
        self.aluno.usuario.save()
        url = reverse(self.get_me_aluno)
        response = self.client.post(url, self.data3, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
