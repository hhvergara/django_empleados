# Generated by Django 3.1.2 on 2020-11-02 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0013_auto_20201102_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='short_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
