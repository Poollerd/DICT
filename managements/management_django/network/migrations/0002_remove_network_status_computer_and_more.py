# Generated by Django 4.1.3 on 2022-12-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='network',
            name='status_computer',
        ),
        migrations.AddField(
            model_name='network',
            name='status_network',
            field=models.CharField(choices=[('ใช้ราชการ', 'ใช้ราชการ'), ('ชำรุด', 'ชำรุด'), ('ส่งซ่อม', 'ส่งซ่อม'), ('เบิกเปลี่ยน', 'เบิกเปลี่ยน')], default='ใช้ราชการ', max_length=20, verbose_name='สถานภาพอุปกรณ์'),
        ),
        migrations.AlterField(
            model_name='network',
            name='person_responsible',
            field=models.CharField(max_length=10, verbose_name='จนท.ผู้รับผิดชอบ'),
        ),
        migrations.AlterField(
            model_name='network',
            name='person_responsible_phone',
            field=models.CharField(max_length=10, verbose_name='เบอร์โทรติดต่อ'),
        ),
    ]