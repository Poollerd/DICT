# Generated by Django 4.1.3 on 2022-12-05 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_install_place', models.CharField(max_length=100, verbose_name='สถานที่ติดตั้งอุปกรณ์')),
                ('computer_type', models.CharField(choices=[('notbook', 'notebook'), ('pc', 'pc'), ('pcserver', 'pc server')], default='pc', max_length=10)),
                ('computer_name', models.CharField(max_length=100, verbose_name='ชื่อเครื่องคอมพิวเตอร์')),
                ('computer_brand', models.CharField(choices=[('handmake', 'handmake'), ('acer', 'acer'), ('hp', 'hp'), ('lenovo', 'lenovo'), ('svoa', 'svoa')], default='', max_length=10, verbose_name='ยี่ห้อของอุปกรณ์')),
                ('computer_series', models.CharField(max_length=20, verbose_name='รุ่นของอุปกรณ์')),
                ('computer_number_rtaf', models.CharField(max_length=20, verbose_name='หมายเลขพัสดุ ทอ')),
                ('computer_series_number', models.CharField(max_length=30, verbose_name='Serial number')),
                ('cpu_brand', models.CharField(choices=[('handmake', 'handmake'), ('acer', 'acer'), ('hp', 'hp'), ('lenovo', 'lenovo'), ('svoa', 'svoa')], default='', max_length=10, verbose_name='ยี่ห้อของ CPU')),
                ('cpu_model', models.CharField(choices=[('amd', 'amd'), ('intel', 'intel')], default='', max_length=10, verbose_name='รุ่นของ CPU')),
                ('cpu_speed_clock', models.CharField(max_length=30, verbose_name='ความเร็วสัญญาณนาฬิกา')),
                ('cpu_unit_speed_clock', models.CharField(max_length=5, verbose_name='หน่วยความเร็วสัญญาณนาฬิกา')),
                ('computer_mac_address', models.CharField(max_length=18, verbose_name='MAC Address')),
                ('computer_use_network', models.CharField(max_length=18, verbose_name='เครื่องข่ายที่ใช้')),
                ('ram_type', models.CharField(max_length=10, verbose_name='RAM')),
                ('ram_capacity', models.CharField(max_length=10, verbose_name='ความจุ RAM')),
                ('ram_unit_capacity', models.CharField(max_length=10, verbose_name='หน่วย RAM')),
                ('harddisk_type_1', models.CharField(max_length=10, verbose_name='ประเภท Harddisk')),
                ('harddisk_capacity_1', models.CharField(max_length=10, verbose_name='ความจุของ Harddisk')),
                ('harddisk_unit_1', models.CharField(max_length=10, verbose_name='หน่วย Harddisk')),
                ('harddisk_type_2', models.CharField(max_length=10, verbose_name='ประเภท Harddisk')),
                ('harddisk_capacity_2', models.CharField(max_length=10, verbose_name='ความจุของ Harddisk')),
                ('harddisk_unit_2', models.CharField(max_length=10, verbose_name='หน่วย Harddisk')),
                ('os_computer', models.CharField(max_length=10, verbose_name='ชื่อระบบปฏิบัติการ')),
                ('os_copyright', models.CharField(max_length=10, verbose_name='ลิขสิทธิ์ของระบบปฏิบัติการ')),
                ('office_name', models.CharField(max_length=10, verbose_name='ชื่อโปรแกรมสำนักงาน')),
                ('office_model_year', models.CharField(max_length=10, verbose_name='รุ่นโปรแกรม')),
                ('office_copyright', models.CharField(max_length=10, verbose_name='ลิขสิทธิ์ของโปรแกรมสำนักงาน')),
                ('antivirus_name', models.CharField(max_length=10, verbose_name='ชื่อโปรแกรมป้องกันไวรัส')),
                ('antivirus_copyright', models.CharField(max_length=10, verbose_name='ลิขสิทธิ์ของโปรแกรม')),
                ('computer_acquisition', models.CharField(max_length=10, verbose_name='คอมพิวเตอร์จากโครงการ')),
                ('computer_start_use_year', models.CharField(max_length=10, verbose_name='เริ่ใใช้เครื่อง พ.ศ.?')),
                ('person_responsible', models.CharField(max_length=10, verbose_name='ผู้รับผิดชอบ')),
                ('person_responsible_phone', models.CharField(max_length=10, verbose_name='ประเภท Harddisk')),
                ('status_computer', models.CharField(choices=[('ใช้ราชการ', 'ใช้ราชการ'), ('ชำรุด', 'ชำรุด'), ('ส่งซ่อม', 'ส่งซ่อม'), ('เบิกเปลี่ยน', 'เบิกเปลี่ยน')], default='ใช้ราชการ', max_length=20, verbose_name='รุ่นของ CPU')),
                ('note', models.CharField(max_length=100, verbose_name=' หมายเหตุ')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computers', to=settings.AUTH_USER_MODEL)),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computers', to='team.team')),
            ],
        ),
    ]
