# Generated by Django 4.1.7 on 2023-02-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0004_remove_parking_cubierto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='num_plazas_discap',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='parking',
            name='num_plazas_grandes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='parking',
            name='num_plazas_peq',
            field=models.IntegerField(default=0),
        ),
    ]
