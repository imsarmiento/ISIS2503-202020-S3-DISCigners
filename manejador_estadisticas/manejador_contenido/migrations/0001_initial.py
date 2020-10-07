# Generated by Django 3.1.2 on 2020-10-07 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manejador_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_conexion', models.CharField(choices=[('AP', 'Api'), ('MD', 'Metadatos'), ('CR', 'Correo')], max_length=2)),
                ('universidaddes', models.ManyToManyField(to='manejador_usuarios.Universidad')),
            ],
        ),
        migrations.CreateModel(
            name='Booklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manejador_contenido.booklist')),
                ('contenidos', models.ManyToManyField(to='manejador_contenido.Contenido')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manejador_usuarios.estudiante')),
            ],
        ),
    ]
