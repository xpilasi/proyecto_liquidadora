# Generated by Django 4.0.5 on 2022-09-23 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_base', '0024_alter_tabladesiniestros_estado_siniestro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabladesiniestros',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
