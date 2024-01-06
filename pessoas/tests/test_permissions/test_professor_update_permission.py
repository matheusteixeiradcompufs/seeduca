from django.urls import reverse
from rest_framework import status

from escolas.models import Disciplina, Turma, Sala
from pessoas.models import Boletim, Avaliacao
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class ProfessorUpdatePermissionTest(PessoasAPITestBase):
    def logar_professor(self):
        self.make_authenticate(self.funcionario)
        self.funcionario.usuario.groups.add(self.grupo_professores)

    def logar_coordenador(self):
        self.make_authenticate(self.funcionario)
        self.funcionario.usuario.groups.add(self.grupo_coordenadores)

    def logar_diretor(self):
        self.make_authenticate(self.funcionario)
        self.funcionario.usuario.groups.add(self.grupo_diretores)

    def setUp(self) -> None:

        super_setup = super(ProfessorUpdatePermissionTest, self).setUp()

        self.basenamelist = 'pessoas:aluno-boletim-avaliacao-api-list'
        self.basenamedetail = 'pessoas:aluno-boletim-avaliacao-api-detail'

        boletim = Boletim.objects.create(
            ano=2000,
            aluno=self.aluno,
        )
        disciplina = Disciplina.objects.create(
            nome='Teste'
        )
        turma = Turma.objects.create(
            nome='Turma Teste',
            ano=2000,
            turno='manha',
            sala=Sala.objects.create(
                numero=0,
                escola=self.make_escola(
                    cnpj='77777777777777'
                )
            )
        )

        self.data_instance = {
            'nome': 'Teste',
            'nota': 0,
            'aluno': self.aluno,
            'boletim': boletim,
            'disciplina': disciplina,
            'turma': turma,
        }

        self.data_instance2 = {
            'nome': 'Teste 2',
            'nota': 0,
            'aluno': self.aluno.id,
            'boletim': boletim.id,
            'disciplina': disciplina.id,
            'turma': turma.id,
        }

        self.data_instance_update = {
            'nota': '10',
        }

        self.instance = Avaliacao.objects.create(**self.data_instance)

        return super_setup

    def test_if_professores_can_list_avaliacoes(self):
        self.logar_professor()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_can_retrieve_avaliacoes(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_can_update_avaliacoes(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_professores_cant_create_avaliacoes(self):
        self.logar_professor()
        url = reverse(self.basenamelist)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_professores_cant_destroy_avaliacoes(self):
        self.logar_professor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_if_coordenadores_can_list_avaliacoes(self):
        self.logar_coordenador()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_create_avaliacoes(self):
        self.logar_coordenador()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_coordenadores_can_retrieve_avaliacoes(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_update_avaliacoes(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_coordenadores_can_destroy_avaliacoes(self):
        self.logar_coordenador()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_if_diretores_can_list_avaliacoes(self):
        self.logar_diretor()
        url = reverse(self.basenamelist)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_can_create_avaliacoes(self):
        self.logar_diretor()
        url = reverse(self.basenamelist)
        response = self.client.post(url, self.data_instance2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_if_diretores_can_retrieve_avaliacoes(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_can_update_avaliacoes(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.patch(url, self.data_instance_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_diretores_can_destroy_avaliacoes(self):
        self.logar_diretor()
        url = reverse(self.basenamedetail, kwargs={'pk': self.instance.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)