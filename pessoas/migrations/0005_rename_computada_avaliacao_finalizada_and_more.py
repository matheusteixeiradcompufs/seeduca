# Generated by Django 4.2.7 on 2024-02-07 22:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0004_alter_funcionario_options_aluno_retrato_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='computada',
            new_name='finalizada',
        ),
        migrations.RenameField(
            model_name='pessoa',
            old_name='escola',
            new_name='escolas',
        ),
        migrations.AddField(
            model_name='media',
            name='atualizada_em',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='media',
            name='criada_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
