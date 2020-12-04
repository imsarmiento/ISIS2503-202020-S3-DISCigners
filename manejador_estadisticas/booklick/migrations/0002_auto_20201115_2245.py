# Generated by Django 3.1.3 on 2020-11-15 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booklick', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadistica',
            name='nombre',
            field=models.CharField(choices=[('BR', 'Booklist por rango'), ('BP', 'Booklist promedio'), ('BC', 'Booklist por carrera'), ('UC', 'Proveedores por carrera para una Universidad'), ('UP', 'Proveedores promedio para una Universidad')], max_length=2),
        ),
        migrations.CreateModel(
            name='ValorTipo2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atributo_carrera', models.CharField(max_length=100)),
                ('atributo_proveedor', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
                ('estadistica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booklick.estadistica')),
            ],
        ),
    ]
