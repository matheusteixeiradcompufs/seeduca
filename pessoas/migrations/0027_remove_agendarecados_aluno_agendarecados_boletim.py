# Generated by Django 4.2.7 on 2024-03-23 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0026_remove_recado_boletim_recado_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendarecados',
            name='aluno',
        ),
        migrations.AddField(
            model_name='agendarecados',
            name='boletim',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='boletim_agendas', to='pessoas.boletim'),
            preserve_default=False,
        ),
    ]