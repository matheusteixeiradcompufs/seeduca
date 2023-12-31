# Generated by Django 4.2.7 on 2024-01-07 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0005_alter_cardapiomerenda_turno'),
        ('pessoas', '0009_alter_dialetivo_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='computada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nome',
            field=models.CharField(choices=[('A1', '1ª Avaliação'), ('A2', '2ª Avaliação'), ('R1', '1ª Recuperação'), ('A3', '3ª Avaliação'), ('A4', '4ª Avaliação'), ('R2', '2ª Recuperação')], max_length=100),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='percentual',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('M1', 'Média 1'), ('M2', 'Média 2'), ('MG', 'Média Geral')], max_length=100)),
                ('valor', models.FloatField(blank=True, null=True)),
                ('boletim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boletim_medias', to='pessoas.boletim')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplina_medias', to='escolas.disciplina')),
            ],
            options={
                'verbose_name': 'média',
                'verbose_name_plural': 'médias',
                'unique_together': {('tipo', 'disciplina', 'boletim')},
            },
        ),
    ]
