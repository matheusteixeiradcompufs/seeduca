# Generated by Django 4.2.7 on 2024-02-09 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0007_alter_pessoa_escolas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='finalizada',
            new_name='confirmar',
        ),
    ]
