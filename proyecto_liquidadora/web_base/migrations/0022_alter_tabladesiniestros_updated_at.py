# Generated by Django 4.0.5 on 2022-09-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_base', '0021_tabladesiniestros_estado_siniestro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabladesiniestros',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Última actualización'),
        ),
    ]
