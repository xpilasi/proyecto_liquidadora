# Generated by Django 4.0.5 on 2022-09-13 12:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web_base', '0012_tabladesiniestros'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tabladesiniestros',
            options={'verbose_name': 'Ingreso de siniestro', 'verbose_name_plural': 'Ingreso de siniestros'},
        ),
        migrations.RemoveField(
            model_name='tabladesiniestros',
            name='nombre',
        ),
        migrations.AddField(
            model_name='tabladesiniestros',
            name='apellido_conductor',
            field=models.CharField(default='', max_length=100, verbose_name='Apellido conductor(a)'),
        ),
        migrations.AddField(
            model_name='tabladesiniestros',
            name='descripcion_siniestro',
            field=models.TextField(default='', max_length=300, verbose_name='Descripción siniestro'),
        ),
        migrations.AddField(
            model_name='tabladesiniestros',
            name='edad_conductor',
            field=models.IntegerField(default=18, verbose_name='Edad conductor(a)'),
        ),
        migrations.AddField(
            model_name='tabladesiniestros',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha registro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tabladesiniestros',
            name='fecha_siniestro',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha siniestro'),
        ),
        migrations.AddField(
            model_name='tabladesiniestros',
            name='nombre_conductor',
            field=models.CharField(default='', max_length=100, verbose_name='Nombre conductor(a)'),
        ),
        migrations.AddField(
            model_name='tabladesiniestros',
            name='nombre_marca',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web_base.marca', verbose_name='Marca vehículo'),
        ),
        migrations.AddField(
            model_name='tabladesiniestros',
            name='rut_conductor',
            field=models.CharField(default='', max_length=100, verbose_name='Rut conductor(a)'),
        ),
        migrations.AddField(
            model_name='tabladesiniestros',
            name='tipo_de_poliza',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web_base.tipopoliza', verbose_name='Póliza contratada'),
        ),
        migrations.AddField(
            model_name='tabladesiniestros',
            name='tipo_de_vehiculo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web_base.tipovehiculo', verbose_name='Tipo de vehículo'),
        ),
        migrations.AlterField(
            model_name='tabladesiniestros',
            name='tipo_de_modelo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web_base.modelovehiculo', verbose_name='Modelo vehículo'),
        ),
        migrations.AlterField(
            model_name='tabladesiniestros',
            name='tipo_de_siniestro',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='web_base.tiposiniestro', verbose_name='Tipo de siniestro'),
        ),
    ]