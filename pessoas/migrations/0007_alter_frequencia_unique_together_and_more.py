# Generated by Django 4.2.7 on 2023-12-30 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0006_alter_boletim_ano_alter_boletim_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='frequencia',
            unique_together={('ano', 'aluno')},
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='nome',
        ),
    ]
