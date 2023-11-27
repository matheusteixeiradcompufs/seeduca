import os

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from escolas.models import Escola


def deletar_imagem(instance):
    try:
        os.remove(instance.imagem.path)
    except (ValueError, FileNotFoundError):
        ...


@receiver(pre_delete, sender=Escola)
def deletar_imagem_escola(sender, instance, *args, **kwargs):
    old_instance = Escola.objects.get(pk=instance.pk)
    deletar_imagem(old_instance)


@receiver(pre_save, sender=Escola)
def atualizar_imagem_escola(sender, instance, *args, **kwargs):
    if instance.pk:
        old_instance = Escola.objects.get(pk=instance.pk)
        eh_nova_imagem = old_instance.imagem != instance.imagem

        if eh_nova_imagem:
            deletar_imagem(old_instance)