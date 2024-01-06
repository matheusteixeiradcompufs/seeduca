import io

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from django.contrib.auth.models import User, Group

from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from escolas.models import Escola
from escolas.signals import deletar_imagem_escola
from pessoas.models import Aluno, Funcionario


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

    def get_auth_data(self, username='user', password='pass', is_superuser=True):
        userdata = {
            'username': username,
            'password': password,
            'is_superuser': is_superuser
        }
        user = self.make_usuario(
            username=userdata.get('username'),
            password=userdata.get('password'),
            is_superuser=userdata.get('is_superuser'),
        )
        response = self.client.post(
            reverse('token_obtain_pair'), data={**userdata}
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

        usuario_funcionario = {
            'username': 'funcionarioteste',
            'password': '12345678',
            'is_superuser': False
        }

        escola = {
            'cnpj': '00000000000001',
            'nome': 'Nova Escola Teste',
        }

        self.grupo_professores = self.make_grupo('Professores')
        self.grupo_coordenadores = self.make_grupo('Coordenadores')
        self.grupo_diretores = self.make_grupo('Diretores')

        self.funcionario = self.make_funcionario(
            usuario_data=usuario_funcionario,
            escola_data=escola,
        )

        self.usuario = self.make_usuario(
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

        self.data_create_funcionario = {
            "matricula": "0000000199",
            "cpf": "88888889993",
            "escola": 1,
            "objeto_usuario": {
                "first_name": "PrimeiroNomeTeste199",
                "last_name": "SobrenomeTeste199",
                "email": "email199@teste.com",
                "username": "usernameteste199",
                "password": "Abcd2341"
            }
        }

        self.data_create_professor = {
            "matricula": "0000000299",
            "cpf": "88888899993",
            "escola": 1,
            "grupos_add": ["Professores"],
            "objeto_usuario": {
                "first_name": "PrimeiroNomeTeste299",
                "last_name": "SobrenomeTeste299",
                "email": "email299@teste.com",
                "username": "usernameteste299",
                "password": "Abcd2341"
            }
        }

        self.data_create_coordenador = {
            "matricula": "0000000499",
            "cpf": "88888899994",
            "escola": 1,
            "grupos_add": ["Coordenadores"],
            "objeto_usuario": {
                "first_name": "PrimeiroNomeTeste499",
                "last_name": "SobrenomeTeste499",
                "email": "email499@teste.com",
                "username": "usernameteste499",
                "password": "Abcd2341"
            }
        }

        self.data_create_diretor = {
            "matricula": "0000000599",
            "cpf": "88888899995",
            "escola": 1,
            "grupos_add": ["Diretores"],
            "objeto_usuario": {
                "first_name": "PrimeiroNomeTeste599",
                "last_name": "SobrenomeTeste599",
                "email": "email599@teste.com",
                "username": "usernameteste599",
                "password": "Abcd2341"
            }
        }

        self.data_update_funcionario = {
            "matricula": "1000000200",
            "cpf": "18888889994",
            "objeto_usuario": {
                "first_name": "PrimeiroNomeTeste1200",
                "last_name": "SobrenomeTeste1200",
                "email": "email1200@teste.com",
            }
        }

        self.data_update_professor = {
            "matricula": "0002000300",
            "cpf": "28888899994",
            "objeto_usuario": {
                "first_name": "PrimeiroNomeTeste2300",
                "last_name": "SobrenomeTeste2300",
                "email": "email2300@teste.com",
            }
        }

        self.escola = self.make_escola(**{'cnpj': '11111111111122'})

        # Gera token de acesso para o usuário normal
        self.make_authenticate(self.usuario)

        return super().setUp()

    def tearDown(self):
        # Certificar-se de que a imagem de teste seja excluída após os testes
        if Escola.objects.filter(pk=self.escola.pk).exists():
            deletar_imagem_escola(sender=None, instance=self.escola)