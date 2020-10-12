# Generated by Django 3.1.2 on 2020-10-11 23:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manejador_contenido', '0001_initial'),
        ('manejador_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('contenido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manejador_contenido.contenido')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manejador_usuarios.estudiante')),
            ],
        ),
    ]
