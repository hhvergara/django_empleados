# Generated by Django 3.1.2 on 2020-11-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0008_auto_20201102_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre'),
        ),
    ]
