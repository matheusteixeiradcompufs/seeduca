# Generated by Django 4.2.7 on 2024-02-17 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0021_alter_boletim_frequencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boletim',
            name='frequencia',
        ),
        migrations.AddField(
            model_name='frequencia',
            name='boletim',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoas.boletim'),
        ),
    ]
