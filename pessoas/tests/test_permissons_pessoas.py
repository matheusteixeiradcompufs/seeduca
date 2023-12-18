from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.reverse import reverse

from pessoas.tests.test_base_pessoas import PessoasTestBase


class PessoasPermissionTest(PessoasTestBase):
    def setUp(self) -> None:
        # Criar um aluno e uma URL para a view
        usuario_data = {
            'first_name': 'TesteName',
            'last_name': 'TesteLastName',
            'username': 'TesteUserName',
            'email': 'testname@email.com',
            'password': '123456'
        }
        escola_data = {
            'cnpj': '00000000000002',
            'nome': 'Escola Teste',
            'endereco': 'Teste',
            'num_salas': 10,
            'descricao': 'Teste'
        }
        self.aluno_teste = self.make_aluno(
            matricula='0000000003',
            cpf='00000000003',
            data_nascimento='1990-01-01',
            endereco='Teste',
            usuario_data=usuario_data,
            escola_data=escola_data,
        )

        return super(PessoasPermissionTest, self).setUp()

    def test_if_alunos_cant_list_create_update_destroy_alunos(self):

        self.user = self.aluno.usuario

        url = reverse('pessoas:aluno-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = reverse('pessoas:aluno-api-list')

        response = self.client.post(url, self.data_create_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})

        response = self.client.patch(url, self.data_update_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_alunos_can_retrive_own_register(self):

        self.user = self.aluno.usuario

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_alunos_cant_retrive_others_alunos(self):

        self.user = self.aluno.usuario

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_can_list_retrive_alunos(self):

        self.user = self.funcionario.usuario

        # Adicionar o usuário ao grupo Professores e tentar acessar a URL do aluno
        grupo_professores = Group.objects.get(name='Professores')
        self.user.groups.add(grupo_professores)

        url = reverse('pessoas:aluno-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_test(self):
        # Autenticar como um usuário normal (sem grupo) e tentar acessar a URL do aluno
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Tentar acessar a URL sem autenticação deve resultar em status 401 Unauthorized
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_funcionario_permission(self):
        # Criar um funcionário e uma URL para a view
        funcionario = self.make_funcionario()
        url = reverse('sua_view_para_funcionario', kwargs={'pk': funcionario.pk})

        # Tentar acessar a URL sem autenticação deve resultar em status 401 Unauthorized
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Autenticar como um usuário normal (sem grupo) e tentar acessar a URL do funcionário
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Adicionar o usuário ao grupo Coordenadores e tentar acessar a URL do funcionário
        grupo_coordenadores = Group.objects.get(name='Coordenadores')
        self.user.groups.add(grupo_coordenadores)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Adicionar o usuário ao grupo Diretores e tentar acessar a URL do funcionário
        grupo_diretores = Group.objects.get(name='Diretores')
        self.user.groups.add(grupo_diretores)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Remover o usuário do grupo Diretores e tentar acessar a URL do funcionário
        self.user.groups.remove(grupo_diretores)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Autenticar como superusuário e tentar acessar a URL do funcionário
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.get_auth_data(username="adminuser")["jwt_access_token"]}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)