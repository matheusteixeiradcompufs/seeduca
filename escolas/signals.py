import os

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from escolas.models import Escola


def deletar_imagem(instance):
    """
    Função para excluir o arquivo de imagem associado à instância do modelo.
    """
    try:
        os.remove(instance.imagem.path)
    except (ValueError, FileNotFoundError):
        # Lida com exceções caso o arquivo não seja encontrado ou não exista
        # Aqui poderia ser adicionado um registro de log para acompanhar essas falhas.
        pass


@receiver(pre_delete, sender=Escola)
def deletar_imagem_escola(sender, instance, *args, **kwargs):
    """
    Signal receiver para excluir a imagem associada a uma instância de Escola antes da exclusão.
    """
    old_instance = Escola.objects.get(pk=instance.pk)
    # Obtém a instância antiga para garantir que o arquivo de imagem será excluído corretamente
    deletar_imagem(old_instance)


@receiver(pre_save, sender=Escola)
def atualizar_imagem_escola(sender, instance, *args, **kwargs):
    """
    Signal receiver para atualizar a imagem associada a uma instância de Escola antes da alteração.
    """
    if instance.pk:
        # Verifica se é uma atualização de uma instância existente
        old_instance = Escola.objects.get(pk=instance.pk)
        eh_nova_imagem = old_instance.imagem != instance.imagem
        # Verifica se a imagem foi alterada

        if eh_nova_imagem:
            # Se a imagem foi alterada, exclui a imagem antiga
            deletar_imagem(old_instance)
