# Generated by Django 4.1.7 on 2023-02-27 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plantas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('id_planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantas.planta')),
            ],
            options={
                'verbose_name': 'zona',
                'verbose_name_plural': 'zonas',
            },
        ),
    ]
