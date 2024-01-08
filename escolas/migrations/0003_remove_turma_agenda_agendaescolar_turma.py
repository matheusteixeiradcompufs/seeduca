# Generated by Django 4.2.7 on 2023-12-31 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0002_alter_agendaescolar_options_alter_diaagenda_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='agenda',
        ),
        migrations.AddField(
            model_name='agendaescolar',
            name='turma',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='turma_agenda', to='escolas.turma'),
            preserve_default=False,
        ),
    ]