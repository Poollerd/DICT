# Generated by Django 4.1.3 on 2022-12-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='computer_brand',
            field=models.CharField(choices=[('handmake', 'Handmake'), ('acer', 'Acer'), ('hp', 'Hp'), ('lenovo', 'Lenovo'), ('svoa', 'SVOA')], default='', max_length=10, verbose_name='ยี่ห้อของอุปกรณ์'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='cpu_brand',
            field=models.CharField(choices=[('handmake', 'Handmake'), ('acer', 'Acer'), ('hp', 'Hp'), ('lenovo', 'Lenovo'), ('svoa', 'SVOA')], default='', max_length=10, verbose_name='ยี่ห้อของ CPU'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='cpu_model',
            field=models.CharField(choices=[('AMD', 'amd'), ('INTEL', 'intel')], default='', max_length=10, verbose_name='รุ่นของ CPU'),
        ),
    ]
