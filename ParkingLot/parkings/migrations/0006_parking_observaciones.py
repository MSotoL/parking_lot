# Generated by Django 4.1.7 on 2023-02-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0005_alter_parking_num_plazas_discap_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='observaciones',
            field=models.CharField(default='', max_length=300, null=True),
        ),
    ]