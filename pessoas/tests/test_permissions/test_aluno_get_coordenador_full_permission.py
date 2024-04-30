from django.urls import reverse
from rest_framework import status

from escolas.models import Sala, Turma
from pessoas.models import Transporte
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class AlunoGetCoordenadorFullPermissionTest(PessoasAPITestBase):
    def logar_aluno(self):
        self.make_authenticate(self.aluno)

    def logar_professor(self):
        self.make_authenticate(self.funcionario)
        self.funcionario.usuario.groups.set([self.grupo_professores.id])

    def logar_coordenador(self):
        self.make_authenticate(self.funcionario)
        self.funcionario.usuario.groups.add(self.grupo_coordenadores)

    def logar_diretor(self):
        self.make_authenticate(self.funcionario)
        self.funcionario.usuario.groups.add(self.grupo_diretores)

    def setUp(self) -> None:
        supersetup = super(AlunoGetCoordenadorFullPermissionTest, self).setUp()

        self.basenamelist = 'escolas:escola-sala-turma-api-list'
        self.basenamedetail = 'escolas:escola-sala-turma-api-detail'

        sala = Sala.objects.create(
            numero=10,
            escola=self.escola,
        )

        self.data_instance = {
            'nome': 'Turma Teste',
            'ano': 2023,
            'turno': 'M',
            'sala': sala,
        }

        self.data_instance2 = {
            'nome': 'Turma Teste 2',
            'ano': 2023,
            'turno': 'T',
            'sala': sala.id,
        }

        self.data_instance_update = {
            'ano': 2024,
        }

        self.instance = Turma.objects.create(**self.data_instance)
        return supersetup

    def test_if_alunos_can_list_turmas(self):
        self.logar_aluno()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_alunos_cant_create_turmas(self):
        self.logar_aluno()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_alunos_can_retrieve_turmas(self):
        self.logar_aluno()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_alunos_cant_update_turmas(self):
        self.logar_aluno()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_alunos_cant_destroy_turmas(self):
        self.logar_aluno()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_can_list_turmas(self):
        self.logar_professor()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_cant_create_turmas(self):
        self.logar_professor()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_can_retrieve_turmas(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_cant_update_turmas(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_destroy_turmas(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenadores_can_list_turmas(self):
        self.logar_coordenador()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_create_turmas(self):
        self.logar_coordenador()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_coordenadores_can_retrieve_turmas(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_update_turmas(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_destroy_turmas(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_diretores_can_list_turmas(self):
        self.logar_diretor()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_can_create_turmas(self):
        self.logar_diretor()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_diretores_can_retrieve_turmas(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_can_update_turmas(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_can_destroy_turmas(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)