# Generated by Django 3.1.2 on 2020-10-12 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manejador_usuarios', '0001_initial'),
    ]

    operations = [
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
            name='Contenido',
            fields=[
                ('titulo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('autor', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('proveedor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manejador_contenido.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Booklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('booklistsContenidos', models.ManyToManyField(blank=True, related_name='_booklist_booklistsContenidos_+', to='manejador_contenido.Booklist')),
                ('contenidos', models.ManyToManyField(blank=True, to='manejador_contenido.Contenido')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manejador_usuarios.estudiante')),
            ],
        ),
    ]
