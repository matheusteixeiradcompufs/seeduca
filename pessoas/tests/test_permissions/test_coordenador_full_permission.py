from django.urls import reverse
from rest_framework import status

from pessoas.models import Transporte
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class CoordenadorFullPermissionTest(PessoasAPITestBase):
    def logar_professor(self):
        self.make_authenticate(self.funcionario)
        self.funcionario.usuario.groups.add(self.grupo_professores)

    def logar_coordenador(self):
        self.make_authenticate(self.funcionario)
        self.funcionario.usuario.groups.add(self.grupo_coordenadores)

    def logar_diretor(self):
        self.make_authenticate(self.funcionario)
        self.funcionario.usuario.groups.add(self.grupo_diretores)

    def setUp(self) -> None:
        supersetup = super(CoordenadorFullPermissionTest, self).setUp()

        self.basenamelist = 'pessoas:aluno-transporte-api-list'
        self.basenamedetail = 'pessoas:aluno-transporte-api-detail'

        self.data_instance = {
            'placa': 'AAA0000',
            'ano': 2023,
        }

        self.data_instance2 = {
            'placa': 'AAA0001',
            'ano': 2023,
        }

        self.data_instance_update = {
            'ano': 2024,
        }

        self.instance = Transporte.objects.create(**self.data_instance)
        return supersetup

    def test_if_professores_cant_list_avaliacoes(self):
        self.logar_professor()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_create_avaliacoes(self):
        self.logar_professor()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_retrieve_avaliacoes(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_update_avaliacoes(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_destroy_avaliacoes(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenadores_can_list_avaliacoes(self):
        self.logar_coordenador()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_create_avaliacoes(self):
        self.logar_coordenador()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_coordenadores_can_retrieve_avaliacoes(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_update_avaliacoes(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_destroy_avaliacoes(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_diretores_can_list_avaliacoes(self):
        self.logar_diretor()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_can_create_avaliacoes(self):
        self.logar_diretor()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_diretores_can_retrieve_avaliacoes(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_can_update_avaliacoes(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_can_destroy_avaliacoes(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)