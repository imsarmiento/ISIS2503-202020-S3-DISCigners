# Generated by Django 3.1.2 on 2020-10-09 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manejador_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='id',
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='carrera',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]