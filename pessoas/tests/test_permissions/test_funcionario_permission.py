from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.reverse import reverse

from pessoas.tests.test_base_pessoas import PessoasTestBase


class PessoasPermissionTest(PessoasTestBase):
    def logar_aluno(self):
        self.make_authenticate(self.aluno.usuario)

    def logar_funcionario(self):
        self.make_authenticate(self.funcionario.usuario)

    def logar_professor(self):
        self.make_authenticate(self.funcionario.usuario)
        self.funcionario.usuario.groups.add(self.grupo_professores)

    def logar_coordenador(self):
        self.make_authenticate(self.funcionario.usuario)
        self.funcionario.usuario.groups.add(self.grupo_coordenadores)

    def logar_diretor(self):
        self.make_authenticate(self.funcionario.usuario)
        self.funcionario.usuario.groups.add(self.grupo_diretores)

    def setUp(self) -> None:
        usuario_data = {
            'first_name': 'TesteName',
            'last_name': 'TesteLastName',
            'username': 'TesteUserName',
            'email': 'testname@email.com',
            'password': '123456'
        }
        self.aluno_teste = self.make_aluno(
            matricula='0000000003',
            cpf='00000000003',
            data_nascimento='1990-01-01',
            endereco='Teste',
            usuario_data=usuario_data,
        )

        self.usuario_data2 = {
            'first_name': 'TesteName2',
            'last_name': 'TesteLastName2',
            'username': 'TesteUserName2',
            'email': 'testname2@email.com',
            'password': '123456'
        }
        self.escola_data2 = {
            'cnpj': '00000000000003',
            'nome': 'Escola Teste',
            'endereco': 'Teste',
            'num_salas': 10,
            'descricao': 'Teste'
        }

        self.funcionario_teste = self.make_funcionario(
            matricula='0000000013',
            cpf='00000000013',
            data_nascimento='1990-01-01',
            endereco='Teste',
            usuario_data=self.usuario_data2,
        )

        return super(PessoasPermissionTest, self).setUp()

    def test_if_alunos_cant_list_funcionarios(self):
        self.logar_aluno()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_alunos_cant_create_funcionarios(self):
        self.logar_aluno()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_alunos_cant_retrieve_funcionarios(self):
        self.logar_aluno()
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_alunos_cant_update_funcionarios(self):
        self.logar_aluno()
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_alunos_cant_destroy_funcionarios(self):
        self.logar_aluno()
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_can_list_retrive_alunos(self):
        self.logar_professor()
        url = reverse('pessoas:aluno-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_can_retrieve_alunos(self):
        self.logar_professor()
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_cant_create_alunos(self):
        self.logar_professor()
        url = reverse('pessoas:aluno-api-list')
        response = self.client.post(url, self.data_create_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_update_alunos(self):
        self.logar_professor()
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno_teste.id})
        response = self.client.patch(url, self.data_update_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_destroy_alunos(self):
        self.logar_professor()
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno_teste.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_can_list_funcionarios(self):
        self.logar_professor()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_cant_create_funcionarios(self):
        self.logar_professor()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_update_funcionarios(self):
        self.logar_professor()
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_destroy_funcionarios(self):
        self.logar_professor()
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professor_can_retrive_own_register(self):
        self.logar_professor()
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_cant_retrive_others_professores(self):
        self.logar_professor()
        self.funcionario_teste.usuario.groups.add(self.grupo_professores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_professores_cant_retrieve_coordenadores(self):
        self.logar_professor()
        self.funcionario_teste.usuario.groups.add(self.grupo_coordenadores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ir_professores_cant_retrieve_diretores(self):
        self.logar_professor()
        self.funcionario_teste.usuario.groups.add(self.grupo_diretores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_coordenadors_can_list_alunos(self):
        self.logar_coordenador()
        url = reverse('pessoas:aluno-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_create_alunos(self):
        self.logar_coordenador()
        url = reverse('pessoas:aluno-api-list')
        response = self.client.post(url, self.data_create_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_coordenadores_can_retrieve_alunos(self):
        self.logar_coordenador()
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_update_alunos(self):
        self.logar_coordenador()
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.patch(url, self.data_update_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_destroy_alunos(self):
        self.logar_coordenador()
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_coordenadores_can_list_professores(self):
        self.logar_coordenador()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_create_professores(self):
        self.logar_coordenador()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_professor, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_coordenadores_can_retrieve_professores(self):
        self.logar_coordenador()
        self.funcionario_teste.usuario.groups.add(self.grupo_professores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_update_professores(self):
        self.logar_coordenador()
        self.funcionario_teste.usuario.groups.add(self.grupo_professores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_destroy_professores(self):
        self.logar_coordenador()
        self.funcionario_teste.usuario.groups.add(self.grupo_professores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_coordenador_cant_create_coordenadores(self):
        self.logar_coordenador(),
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_coordenador, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenador_cant_create_diretores(self):
        self.logar_coordenador()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_diretor, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenador_can_list_professores_and_own_register(self):
        self.logar_coordenador()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_coordenador_can_retrieve_own_register(self):
        self.logar_coordenador()
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenador_cant_update_coordenadores(self):
        self.logar_coordenador()
        self.funcionario_teste.usuario.groups.add(self.grupo_coordenadores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_coordenador_cant_update_diretores(self):
        self.logar_coordenador()
        self.funcionario_teste.usuario.groups.add(self.grupo_diretores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_coordenador_cant_destroy_coordenadores(self):
        self.logar_coordenador()
        self.funcionario_teste.usuario.groups.add(self.grupo_coordenadores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_coordenador_cant_destroy_diretores(self):
        self.logar_coordenador()
        self.funcionario_teste.usuario.groups.add(self.grupo_diretores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_diretor_can_list_alunos(self):
        self.logar_diretor()
        url = reverse('pessoas:aluno-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_can_create_alunos(self):
        self.logar_diretor()
        url = reverse('pessoas:aluno-api-list')
        response = self.client.post(url, self.data_create_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_diretor_can_retrieve_alunos(self):
        self.logar_diretor()
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_can_update_alunos(self):
        self.logar_diretor()
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.patch(url, self.data_update_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_can_destroy_alunos(self):
        self.logar_diretor()
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_diretor_can_list_professores_and_coordenadores(self):
        self.logar_diretor()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_can_create_professores(self):
        self.logar_diretor()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_professor, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_diretor_can_retrieve_professores(self):
        self.logar_diretor()
        self.funcionario_teste.usuario.groups.add(self.grupo_professores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_can_update_professores(self):
        self.logar_diretor()
        self.funcionario_teste.usuario.groups.add(self.grupo_professores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_can_destroy_professores(self):
        self.logar_diretor()
        self.funcionario_teste.usuario.groups.add(self.grupo_professores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_diretor_can_create_coordenadores(self):
        self.logar_diretor()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_coordenador, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_diretor_can_retrieve_coordenadores(self):
        self.logar_diretor()
        self.funcionario_teste.usuario.groups.add(self.grupo_coordenadores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_can_update_coordenadores(self):
        self.logar_diretor()
        self.funcionario_teste.usuario.groups.add(self.grupo_coordenadores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_can_destroy_coordenadores(self):
        self.logar_diretor()
        self.funcionario_teste.usuario.groups.add(self.grupo_coordenadores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_diretor_can_list(self):
        self.logar_diretor()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_can_retrieve_own_register(self):
        self.logar_diretor()
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_cant_create_diretores(self):
        self.logar_diretor()
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_diretor, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_diretor_cant_update_diretores(self):
        self.logar_diretor()
        self.funcionario_teste.usuario.groups.add(self.grupo_diretores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_diretor_cant_destroy_diretores(self):
        self.logar_diretor()
        self.funcionario_teste.usuario.groups.add(self.grupo_diretores)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_non_valid_usuarios_cant_create_diretores(self):
        self.make_authenticate(self.funcionario)
        grupo_teste = Group.objects.create(name='Teste')
        self.funcionario.usuario.groups.add(grupo_teste)
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_diretor, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_non_valid_usuarios_cant_retrieve_usuarios(self):
        self.logar_diretor()
        grupo_teste = Group.objects.create(name='Teste')
        self.funcionario_teste.usuario.groups.add(grupo_teste)
        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_funcionarios_with_no_groups_returns_queryset_none(self):
        self.logar_funcionario()
        grupo = self.make_grupo('Teste')
        self.funcionario.usuario.groups.add(grupo)
        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.data, [])