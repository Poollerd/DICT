from django.contrib.auth.models import User
from django.db import models

from team.models import Team

class Network(models.Model):

    ACTIVE = 'ใช้ราชการ'
    INACTIVE = 'ชำรุด'
    MANTAINENT = 'ส่งซ่อม'
    CHANGE = 'เบิกเปลี่ยน'


    CHOICES_STATUSNET = (

        (ACTIVE,'ใช้ราชการ'),
        (INACTIVE, 'ชำรุด'),
        (MANTAINENT, 'ส่งซ่อม'),
        (CHANGE, 'เบิกเปลี่ยน'),

    )



    team_name = models.ForeignKey(Team, related_name='networks', on_delete=models.CASCADE)
    network_install_place = models.CharField(max_length=100, verbose_name = "สถานที่ติดตั้ง")
    network_type = models.CharField(max_length=20, verbose_name='ชนิดอุปกรณ์ Rounter Switch ฯลฯ')
    network_brand = models.CharField(max_length=50, verbose_name='ยี่ห้ออุปกรณ์ ex. Cisco  ฯลฯ')
    network_name = models.CharField(max_length=100, verbose_name='ชื่อ/รุ่นอุปกรณ์เครือข่าย',  blank=True)
    network_name_in_system = models.CharField(max_length=50, verbose_name='ชื่ออุปกรณในระบบ, Hostname')
    network_mac_address = models.CharField(max_length=30, verbose_name='MAC Address')
    network_ip_address = models.CharField(max_length=30, verbose_name='IP Address')
    network_got = models.CharField(max_length=100, verbose_name='ที่มาของอุปกรณ์(โครงการ/หน่วยจัดหา/ส่วนตัว)')
    network_serial_number = models.CharField(max_length=18, verbose_name='SERIAL NUMBER')
    network_start_year = models.CharField(max_length=4, verbose_name='เริมใช้อุปกรณ์เครือข่ายปี พ.ศ.')
    network_person_responsible = models.CharField(max_length=50, verbose_name='จนท.ผู้รับผิดชอบ')
    network_person_responsible_phone = models.CharField(max_length=10, verbose_name='เบอร์โทรติดต่อ')
    network_status = models.CharField(max_length=20, verbose_name='สถานภาพอุปกรณ์', choices=CHOICES_STATUSNET, default='ใช้ราชการ')
    network_note = models.CharField(max_length=100, verbose_name=' หมายเหตุ',  blank=True)
    created_by = models.ForeignKey(User, related_name='networks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.network_install_place+' '+ self.network_brand +' '+ self.network_person_responsible +' '+self.network_status 