# Generated by Django 4.1.3 on 2022-12-01 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='department',
            field=models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='สังกัด'),
        ),
    ]
