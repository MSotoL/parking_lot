# Generated by Django 4.1.7 on 2023-02-27 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0001_initial'),
        ('zonas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Planta',
            new_name='Zona',
        ),
    ]
