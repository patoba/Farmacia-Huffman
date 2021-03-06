# Generated by Django 2.0.4 on 2018-05-13 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0005_auto_20180513_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoIndividual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('provedor', models.CharField(max_length=40)),
                ('clasificacion', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
                ('descuento', models.IntegerField(default=0)),
                ('total', models.FloatField(default=0)),
                ('factura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='farmacia.Factura')),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='factura',
        ),
    ]
