from django.urls import reverse
from rest_framework import status

from escolas.models import Disciplina, Turma, Sala
from pessoas.models import Media, Boletim
from pessoas.tests.test_apis.test_api_base import PessoasAPITestBase


class MediaAPITest(PessoasAPITestBase):
    def setUp(self) -> None:
        supersetup = super(MediaAPITest, self).setUp()

        self.basenamelist = 'pessoas:aluno-boletim-media-api-list'
        self.basenamedetail = 'pessoas:aluno-boletim-media-api-detail'

        self.turma = Turma.objects.create(
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
        disciplina = Disciplina.objects.create(
            nome='Teste'
        )
        self.turma.disciplinas.add(disciplina)
        disciplina = Disciplina.objects.create(
            nome='Teste - 2'
        )
        self.turma.disciplinas.add(disciplina)
        self.aluno.turmas.add(self.turma)
        self.boletim = Boletim.objects.create(
            ano=2000,
            aluno=self.aluno,
        )

        # self.data_instance = {
        #     'tipo': 'M1',
        #     'valor': 0,
        #     'boletim': boletim,
        #     'disciplina': disciplina,
        # }
        #
        # self.data_instance2 = {
        #     'tipo': 'M2',
        #     'valor': 0,
        #     'boletim': boletim.id,
        #     'disciplina': disciplina.id,
        # }
        #
        # self.data_instance_update = {
        #     'valor': 5,
        # }
        #
        # self.instance = Media.objects.create(**self.data_instance)
        return supersetup

    # def test_list_media_aluno(self):
    #     self.list_base(self.basenamelist)
    #
    # def test_create_media_aluno(self):
    #     self.create_base(self.data_instance2, self.basenamelist)
    #
    # def test_retrieve_media_aluno(self):
    #     self.retrieve_base(self.instance.id, self.basenamedetail)
    #
    # def test_update_media_aluno(self):
    #     self.update_base(self.instance.id, self.data_instance_update, self.basenamedetail)
    #
    # def test_destroy_media_aluno(self):
    #     self.destroy_base(self.instance.id, self.basenamedetail)

    def test_if_create_boletim_create_medias_too(self):
        disciplinas = self.aluno.turmas.filter(ano=2000).first().disciplinas.all()
        avaliacoes_teste = []
        for disciplina in disciplinas:
            for media in Media.TIPO_MEDIA_CHOICES:
                avaliacoes_teste.append(media[0] + " - " + str(disciplina) + " - " + str(self.aluno))
        cont = 0
        for media in self.boletim.boletim_medias.all():
            self.assertEqual(str(media), avaliacoes_teste[cont])
            cont = cont + 1

    def test_if_list_media_aluno(self):
        self.list_base(self.basenamelist)

    def test_if_retrieve_media_in_boletim(self):
        url = reverse(self.basenamedetail, kwargs={'pk': self.boletim.boletim_medias.first().id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_update_media_in_boletim(self):
        url = reverse(self.basenamedetail, kwargs={'pk': self.boletim.boletim_medias.first().id})
        response = self.client.patch(url, {'valor': 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_if_destoy_media_in_boletim(self):
        url = reverse(self.basenamedetail, kwargs={'pk': self.boletim.boletim_medias.first().id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)