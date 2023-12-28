from rest_framework import status
from rest_framework.reverse import reverse

from pessoas.tests.test_base_pessoas import PessoasTestBase


class PessoasPermissionTest(PessoasTestBase):
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

        self.usuario_data3 = {
            'first_name': 'TesteName3',
            'last_name': 'TesteLastName3',
            'username': 'TesteUserName3',
            'email': 'testname3@email.com',
            'password': '123456'
        }
        self.escola_data3 = {
            'cnpj': '00000000000004',
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
            escola_data=self.escola_data2,
        )
        self.funcionario_teste2 = self.make_funcionario(
            matricula='0000000023',
            cpf='00000000023',
            data_nascimento='1990-01-02',
            endereco='Teste2',
            usuario_data=self.usuario_data3,
            escola_data=self.escola_data3,
        )

        return super(PessoasPermissionTest, self).setUp()

    def test_if_alunos_cant_list_create_update_destroy_alunos(self):

        self.make_authenticate(self.aluno.usuario)

        url = reverse('pessoas:aluno-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.post(url, self.data_create_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})

        response = self.client.patch(url, self.data_update_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_alunos_can_retrive_own_register(self):

        self.make_authenticate(self.aluno.usuario)

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_alunos_cant_retrive_others_alunos(self):

        self.make_authenticate(self.aluno.usuario)

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_can_list_retrive_alunos(self):
        self.logar_professor()

        url = reverse('pessoas:aluno-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_cant_create_update_delete_alunos(self):
        self.logar_professor()

        url = reverse('pessoas:aluno-api-list')
        response = self.client.post(url, self.data_create_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno_teste.id})
        response = self.client.patch(url, self.data_update_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_list_create_update_destroy_funcionarios(self):
        self.logar_professor()

        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK) # CORRIGIR ISSO

        response = self.client.post(url, self.data_create_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})

        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # DESCOBRIR O ERRO
    def test_if_professor_can_retrive_own_register(self):
        self.logar_professor()

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_cant_retrive_others_funcionarios(self):
        self.logar_professor()

        self.funcionario_teste.usuario.groups.add(self.grupo_professores)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self.funcionario_teste.usuario.groups.remove(self.grupo_professores)
        self.funcionario_teste.usuario.groups.add(self.grupo_coordenadores)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self.funcionario_teste.usuario.groups.remove(self.grupo_coordenadores)
        self.funcionario_teste.usuario.groups.add(self.grupo_diretores)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_coordenadors_can_list_create_retrive_update_delete_alunos(self):
        self.logar_coordenador()

        url = reverse('pessoas:aluno-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(url, self.data_create_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch(url, self.data_update_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_coordenadors_can_list_create_retrive_update_delete_professores(self):
        self.logar_coordenador()

        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(url, self.data_create_professor, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.funcionario_teste.usuario.groups.add(self.grupo_professores)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_coordenador_cant_create_coordenadores_and_diretores(self):
        self.logar_coordenador()

        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_coordenador, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.post(url, self.data_create_diretor, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenador_can_list_and_retrive_own_register(self):
        self.logar_coordenador()

        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenador_cant_update_delete_coordenadores_and_diretores(self):
        self.logar_coordenador()

        self.funcionario_teste.usuario.groups.add(self.grupo_coordenadores)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self.funcionario_teste.usuario.groups.remove(self.grupo_coordenadores)
        self.funcionario_teste.usuario.groups.add(self.grupo_diretores)

        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_diretor_can_list_create_retrive_update_delete_alunos(self):
        self.logar_diretor()

        url = reverse('pessoas:aluno-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(url, self.data_create_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch(url, self.data_update_aluno, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_diretor_can_list_create_retrive_update_delete_professores_and_coordenadores(self):
        self.logar_diretor()

        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(url, self.data_create_professor, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(url, self.data_create_coordenador, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.funcionario_teste.usuario.groups.add(self.grupo_professores)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.funcionario_teste2.usuario.groups.add(self.grupo_coordenadores)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste2.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_diretor_can_list_and_retrive_own_register(self):
        self.logar_diretor()

        url = reverse('pessoas:funcionario-api-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretor_cant_create_update_delete_diretores(self):
        self.logar_diretor()

        url = reverse('pessoas:funcionario-api-list')
        response = self.client.post(url, self.data_create_diretor, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.funcionario_teste.usuario.groups.add(self.grupo_diretores)

        url = reverse('pessoas:funcionario-api-detail', kwargs={'pk': self.funcionario_teste.id})
        response = self.client.patch(url, self.data_update_funcionario, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
