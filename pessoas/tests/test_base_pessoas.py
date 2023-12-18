from django.test import TestCase

from django.contrib.auth.models import User, Group

from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from pessoas.models import Aluno, Funcionario

from escolas.tests.test_base_escola import EscolaMixin


class PessoaMixin(EscolaMixin):
    def make_grupo(
            self,
            nome='Grupo',
    ):
        return Group.objects.create(
            name=nome,
        )

    def make_usuario(
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

    def make_aluno(
            self,
            matricula='0000000000',
            cpf='00000000000',
            data_nascimento='1990-01-01',
            endereco='Endereço Teste',
            usuario_data=None,
            escola_data=None,
    ):
        if usuario_data is None:
            usuario_data = {}
        if escola_data is None:
            escola_data = {}
        return Aluno.objects.create(
            matricula=matricula,
            cpf=cpf,
            data_nascimento=data_nascimento,
            endereco=endereco,
            usuario=self.make_usuario(**usuario_data),
            escola=self.make_escola(**escola_data)
        )

    def make_funcionario(
            self,
            matricula='0000000001',
            cpf='00000000001',
            data_nascimento='1990-01-01',
            endereco='Endereço Teste',
            formacao='Formação Teste',
            usuario_data=None,
            escola_data=None,
    ):
        if usuario_data is None:
            usuario_data = {}
        if escola_data is None:
            escola_data = {}
        return Funcionario.objects.create(
            matricula=matricula,
            cpf=cpf,
            data_nascimento=data_nascimento,
            endereco=endereco,
            formacao=formacao,
            usuario=self.make_usuario(**usuario_data),
            escola=self.make_escola(**escola_data),
        )

    def get_auth_data(self, username='user', password='pass'):
        userdata = {
            'username': username,
            'password': password,
        }
        user = self.make_usuario(
            username=userdata.get('username'),
            password=userdata.get('password'),
            is_superuser=True,
        )
        response = self.client.post(
            reverse('recipes:token_obtain_pair'), data={**userdata}
        )
        return {
            'jwt_access_token': response.data.get('access'),
            'jwt_refresh_token': response.data.get('refresh'),
            'user': user,
        }

    def make_authenticate(self, usuario):
        # Gera token de acesso para o usuário normal
        refresh = RefreshToken.for_user(usuario)
        self.access_token = str(refresh.access_token)

        # Configura o cliente da API com o token de acesso
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')


class PessoasTestBase(TestCase, PessoaMixin):
    def setUp(self) -> None:
        # Cria um usuário normal para testar autenticação
        self.aluno = self.make_aluno(usuario_data={'is_superuser': False})

        usuario = {
            'username': 'funcionarioteste',
            'password': '12345678',
            'is_superuser': False
        }

        escola = {
            'cnpj': '00000000000001',
            'nome': 'Nova Escola Teste',
        }

        self.make_grupo('Professores')
        self.make_grupo('Coordenadores')
        self.make_grupo('Diretores')

        self.funcionario = self.make_funcionario(
            usuario_data=usuario,
            escola_data=escola,
        )

        self.user = self.make_usuario(
            first_name='AdminTeste',
            last_name='TesteAdmin',
            username='admintest',
            password='123456',
            email='admintest@test.com',
            is_superuser=True,
        )

        self.data_create_aluno = {
            "matricula": "0000000099",
            "cpf": "88888888993",
            "escola": 1,
            "objeto_usuario": {
                "first_name": "PrimeiroNomeTeste99",
                "last_name": "SobrenomeTeste99",
                "email": "email99@teste.com",
                "username": "usernameteste99",
                "password": "Abcd2341"
            }
        }

        self.data_update_aluno = {
            "matricula": "0000000100",
            "cpf": "88888888994",
            "objeto_usuario": {
                "first_name": "PrimeiroNomeTeste100",
                "last_name": "SobrenomeTeste100",
                "email": "email100@teste.com",
            }
        }

        # Gera token de acesso para o usuário normal
        self.make_authenticate(self.aluno)

        return super().setUp()