# Generated by Django 4.1.7 on 2023-02-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=100)),
                ('cubierto', models.BooleanField(default=True)),
                ('num_plazas_grandes', models.IntegerField()),
                ('num_plazas_peq', models.IntegerField()),
                ('num_plazas_discap', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'parking',
                'verbose_name_plural': 'parkings',
            },
        ),
    ]