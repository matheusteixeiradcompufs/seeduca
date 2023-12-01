
from django.urls import reverse
from rest_framework import status
from escolas.tests.test_base_escola import EscolaTestBase


class EscolaAPITestCase(EscolaTestBase):
    def test_list_escolas(self):
        url = reverse('escolas:escolas-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_escola(self):
        url = reverse('escolas:escolas-api-detail', args=[self.escola.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_retrive_escola_returns_404_if_escola_not_found(self):
        url = reverse('escolas:escolas-api-detail', args=[10])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Adicione mais testes conforme necessário para as operações CRUD

    def test_create_escola(self):
        url = reverse('escolas:escolas-api-list')
        data = {'cnpj': '00000000000001', 'nome': 'Nova Escola', 'endereco': 'Novo Endereço'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_non_superusers_receive_error_403_using_create_escola(self):
        self.user.is_superuser = False
        self.user.save()
        url = reverse('escolas:escolas-api-list')
        data = {'cnpj': '00000000000001', 'nome': 'Nova Escola', 'endereco': 'Novo Endereço'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_incorrect_data_receive_error_400_using_create_escola(self):
        url = reverse('escolas:escolas-api-list')
        data = {'nome': 'Nova Escola', 'endereco': 'Novo Endereço'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_escola(self):
        url = reverse('escolas:escolas-api-detail', args=[self.escola.id])
        data = {'nome': 'Escola Atualizada', 'endereco': 'Endereço Atualizado'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_non_superusers_receive_error_403_using_update_escola(self):
        self.user.is_superuser = False
        self.user.save()
        url = reverse('escolas:escolas-api-detail', args=[self.escola.id])
        data = {'nome': 'Escola Atualizada', 'endereco': 'Endereço Atualizado'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_update_escola_returns_404_if_not_found_escola(self):
        url = reverse('escolas:escolas-api-detail', args=[10])
        data = {'nome': 'Escola Atualizada', 'endereco': 'Endereço Atualizado'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_escola(self):
        url = reverse('escolas:escolas-api-detail', args=[self.escola.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_non_superusers_receive_error_403_using_delete_urls(self):
        self.user.is_superuser = False
        self.user.save()
        url = reverse('escolas:escolas-api-detail', args=[self.escola.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_delete_escola_returns_404_if_not_found_escola (self):
        url = reverse('escolas:escolas-api-detail', args=[10])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
