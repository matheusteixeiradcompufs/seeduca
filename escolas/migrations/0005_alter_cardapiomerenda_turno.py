# Generated by Django 4.2.7 on 2024-01-07 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0004_remove_agendaescolar_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapiomerenda',
            name='turno',
            field=models.CharField(max_length=50),
        ),
    ]
