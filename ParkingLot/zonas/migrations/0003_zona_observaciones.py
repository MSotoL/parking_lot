# Generated by Django 4.1.7 on 2023-02-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0002_rename_planta_zona'),
    ]

    operations = [
        migrations.AddField(
            model_name='zona',
            name='observaciones',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
