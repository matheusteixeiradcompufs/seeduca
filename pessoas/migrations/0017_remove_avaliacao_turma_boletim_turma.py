# Generated by Django 4.2.7 on 2024-02-10 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0006_alter_aviso_diaagenda_alter_avisoescola_mural_and_more'),
        ('pessoas', '0016_remove_pessoa_escolas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='turma',
        ),
        migrations.AddField(
            model_name='boletim',
            name='turma',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='turma_boletins', to='escolas.turma'),
            preserve_default=False,
        ),
    ]
