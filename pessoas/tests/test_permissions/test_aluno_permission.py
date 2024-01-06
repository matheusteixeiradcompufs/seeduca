from django.urls import reverse
from rest_framework import status

from pessoas.tests.test_base_pessoas import PessoasTestBase


class PessoasPermissionTest(PessoasTestBase):
    def logar_aluno(self):
        self.make_authenticate(self.aluno.usuario)

    def setUp(self) -> None:
        super_setup = super(PessoasPermissionTest, self).setUp()

        self.logar_aluno()

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

        return super_setup

    def test_if_alunos_cant_list_create_update_destroy_alunos(self):
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
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_alunos_cant_retrive_others_alunos(self):
        url = reverse('pessoas:aluno-api-detail', kwargs={'pk': self.aluno_teste.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)