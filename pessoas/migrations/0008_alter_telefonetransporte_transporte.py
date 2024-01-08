# Generated by Django 4.2.7 on 2023-12-30 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0007_alter_frequencia_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefonetransporte',
            name='transporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transporte_telefones', to='pessoas.transporte'),
        ),
    ]