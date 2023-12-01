import os
from unittest.mock import patch

from appseeduca.settings import BASE_DIR
from escolas.signals import deletar_imagem_escola, atualizar_imagem_escola, deletar_imagem
from escolas.tests.test_base_escola import EscolaTestBase


class EscolaSignalsTestCase(EscolaTestBase):
    def test_deletar_imagem_escola_signal(self):
        deletar_imagem_escola(sender=None, instance=self.escola)
        self.assertFalse(os.path.exists(self.escola.imagem.url))

    @patch('os.remove')
    def test_deletar_imagem_exception_handling(self, mock_remove):
        # Configurar o mock para simular uma exceção
        mock_remove.side_effect = ValueError("Simulando ValueError")

        # Criar uma instância de Escola para usar nos testes
        escola = self.make_escola(cnpj='11111111111111')
        imagem = BASE_DIR.__str__() + os.path.normpath(escola.imagem.url)

        # Chamar a função deletar_imagem e verificar se a exceção é tratada corretamente
        deletar_imagem(escola)

        # Verificar se os métodos apropriados foram chamados
        mock_remove.assert_called_once_with(imagem)

    def test_atualizar_imagem_escola_conditional(self):
        # Criar uma instância de Escola com uma imagem
        imagem_antiga = self.escola.imagem.url
        self.escola.imagem = self.make_image(nome='nova_imagem.jpg')
        self.escola.save()
        imagem_nova = self.escola.imagem.url

        # Verificar se a condição foi tratada corretamente
        self.assertTrue(os.path.exists(BASE_DIR.__str__() + os.path.normpath(imagem_nova)))
        self.assertFalse(os.path.exists(BASE_DIR.__str__() + os.path.normpath(imagem_antiga)))