# Generated by Django 4.1.7 on 2023-02-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0009_parking_cubierto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='observaciones',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]