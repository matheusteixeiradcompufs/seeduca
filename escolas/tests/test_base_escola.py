import io
from django.test import TestCase

from PIL import Image
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from escolas.models import Escola
from escolas.signals import deletar_imagem_escola
from pessoas.tests.test_base_pessoas import PessoaMixin


class EscolaTestBase(TestCase, PessoaMixin):
    def setUp(self) -> None:
        self.escola = self.make_escola()

        # Cria um usuário normal para testar autenticação
        self.user = self.make_user()

        # Gera token de acesso para o usuário normal
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Configura o cliente da API com o token de acesso
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        return super().setUp()

    def tearDown(self):
        # Certificar-se de que a imagem de teste seja excluída após os testes
        if Escola.objects.filter(pk=self.escola.pk).exists():
            deletar_imagem_escola(sender=None, instance=self.escola)
