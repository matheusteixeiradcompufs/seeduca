# Generated by Django 4.2.7 on 2024-01-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0009_alter_agendaescolar_dias_nao_uteis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendaescolar',
            name='dias_nao_uteis',
        ),
        migrations.AddField(
            model_name='diaagenda',
            name='util',
            field=models.BooleanField(default=False),
        ),
    ]
