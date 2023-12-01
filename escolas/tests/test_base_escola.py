import io
from django.test import TestCase

from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from escolas.models import Escola
from escolas.signals import deletar_imagem_escola


class EscolaMixin:
    def make_image(
            self,
            nome='test_image.jpg',
    ):
        with open("C:\\Users\\matheus.teixeira\\Pictures\\2002261230095343-04.jpg", "rb") as image_file:
            image_bytes = image_file.read()
        # Crie uma imagem temporária em memória
        Image.open(io.BytesIO(image_bytes))
        return SimpleUploadedFile(nome, image_bytes, content_type="image/jpeg")

    def make_user(
            self,
            first_name='User',
            last_name='Name',
            username='username',
            password='123456',
            email='username@email.com',
            is_superuser=True,
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
            is_superuser=is_superuser,
        )

    def make_escola(
            self,
            cnpj='00000000000000',
            nome='Nome de Teste',
            endereco='Endereço de Teste',
            num_salas=10,
            descricao='Descrição de Teste',
    ):
        return Escola.objects.create(
            cnpj=cnpj,
            nome=nome,
            endereco=endereco,
            num_salas=num_salas,
            descricao=descricao,
            imagem=self.make_image()
        )

    def get_auth_data(self, username='user', password='pass'):
        userdata = {
            'username': username,
            'password': password,
        }
        user = self.make_user(
            username=userdata.get('username'),
            password=userdata.get('password')
        )
        response = self.client.post(
            reverse('recipes:token_obtain_pair'), data={**userdata}
        )
        return {
            'jwt_access_token': response.data.get('access'),
            'jwt_refresh_token': response.data.get('refresh'),
            'user': user,
        }


class EscolaTestBase(TestCase, EscolaMixin):
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
