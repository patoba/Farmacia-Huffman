# Generated by Django 2.0.4 on 2018-05-13 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmacia', '0006_auto_20180513_0527'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='monto',
            field=models.FloatField(default=0),
        ),
    ]
