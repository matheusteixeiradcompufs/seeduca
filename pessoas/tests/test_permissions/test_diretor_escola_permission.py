from django.urls import reverse
from rest_framework import status

from escolas.models import Escola
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class DiretorEscolaTest(PessoasAPITestBase):
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
        supersetup = super(DiretorEscolaTest, self).setUp()

        self.basenamelist = 'escolas:escola-api-list'
        self.basenamedetail = 'escolas:escola-api-detail'

        self.data_instance = {
            'cnpj': '11111111111111',
            'nome': 'Nome Teste',
            'endereco': 'Endereço Teste',
        }

        self.data_instance2 = {
            'cnpj': '11111111111112',
            'nome': 'Nome Teste 2',
            'endereco': 'Endereço Teste 2',
        }

        self.data_instance_update = {
            'endereco': 'Atualizado',
        }

        self.instance = Escola.objects.create(**self.data_instance)
        return supersetup

    def test_if_professores_cant_list_escolas(self):
        self.logar_professor()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_create_escolas(self):
        self.logar_professor()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_retrieve_escolas(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_update_escolas(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_destroy_escolas(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenadores_cant_list_escolas(self):
        self.logar_coordenador()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenadores_cant_create_escolas(self):
        self.logar_coordenador()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenadores_cant_retrieve_escolas(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenadores_cant_update_escolas(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenadores_cant_destroy_escolas(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_diretores_can_list_escolas(self):
        self.logar_diretor()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_cant_create_escolas(self):
        self.logar_diretor()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_diretores_can_retrieve_escolas(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_cant_update_escolas(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_diretores_cant_destroy_escolas(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)