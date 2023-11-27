from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from escolas.models import Escola


class EscolaAPITestCase(TestCase):
    def setUp(self):
        # Cria uma escola para usar nos testes
        self.escola = Escola.objects.create(nome='Escola Teste', endereco='Endereço de Teste')

    def test_list_escolas(self):
        url = reverse('escolas:escolas-api-list')
        print('url: ', url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_escola(self):
        url = reverse('escolas:escolas-api-detail', args=[self.escola.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Adicione mais testes conforme necessário para as operações CRUD

    def test_create_escola(self):
        url = reverse('escolas:escolas-api-list')
        data = {'nome': 'Nova Escola', 'endereco': 'Novo Endereço'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # 403 porque apenas superusuários podem criar

    def test_update_escola(self):
        url = reverse('escolas:escolas-api-detail', args=[self.escola.id])
        data = {'nome': 'Escola Atualizada', 'endereco': 'Endereço Atualizado'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # 403 porque apenas superusuários podem atualizar

    def test_delete_escola(self):
        url = reverse('escolas:escolas-api-detail', args=[self.escola.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # 403 porque apenas superusuários podem excluir
