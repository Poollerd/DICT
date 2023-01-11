from django.contrib.auth.models import User
from django.db import models

from team.models import Team

class Computer(models.Model):

    NOTEBOOK = 'notbook'
    PC = 'pc'
    PCSERVER = 'pcserver'

    CHOICES_TYPECOM = (
        (NOTEBOOK, 'notebook'),
        (PC, 'pc'),
        (PCSERVER, 'pc server'),
    )

    HANDMAKE = 'handmake'
    ACER = 'acer'
    HP = 'hp'
    Lenovo = 'lenovo'
    SVOA = 'svoa' 


    CHOICES_BRANDCOM = (

        (HANDMAKE, 'Handmake'),
        (ACER, 'Acer'),
        (HP, 'Hp'),
        (Lenovo, 'Lenovo'),
        (SVOA, 'SVOA'),
    )
    
    AMD = 'AMD'
    INTEL = 'INTEL'
    other = 'Other'


    CHOICES_BRANDCPU = (

        (AMD, 'AMD'),
        (INTEL, 'INTEL'),
        (INTEL, 'Other'),

    )

    ACTIVE = 'ใช้ราชการ'
    INACTIVE = 'ชำรุด'
    MANTAINENT = 'ส่งซ่อม'
    CHANGE = 'เบิกเปลี่ยน'
    SENTBACK = 'ส่งคืน'


    CHOICES_STATUSCOM = (

        (ACTIVE,'ใช้ราชการ'),
        (INACTIVE, 'ชำรุด'),
        (MANTAINENT, 'ส่งซ่อม'),
        (CHANGE, 'เบิกเปลี่ยน'),
        (SENTBACK, 'ส่งคืน'),

    )



    team_name = models.ForeignKey(Team, related_name='computers',verbose_name = "กรม", on_delete=models.CASCADE)
    computer_install_place = models.CharField(max_length=100, verbose_name = "สถานที่ติดตั้งอุปกรณ์", null=False)
    # computer_type = models.CharField(max_length=10, choices=CHOICES_TYPECOM, default=PC)
    computer_type = models.CharField(max_length=10,verbose_name = "ประเภทอุปกรณ์คอมพิวเตอร์")
    computer_name = models.CharField(max_length=100, verbose_name='ชื่อเครื่องคอมพิวเตอร์')
    # computer_brand = models.CharField(max_length=10, verbose_name='ยี่ห้อของอุปกรณ์', choices=CHOICES_BRANDCOM, default='')
    computer_brand = models.CharField(max_length=10, verbose_name='ยี่ห้อของอุปกรณ์')
    computer_series = models.CharField(max_length=20, verbose_name='รุ่นของอุปกรณ์')
    computer_number_rtaf = models.CharField(max_length=17, verbose_name='หมายเลขพัสดุ ทอ')
    computer_series_number = models.CharField(max_length=30, verbose_name='Serial number')
    # cpu_brand = models.CharField(max_length=10, verbose_name='ยี่ห้อของ CPU', choices=CHOICES_BRANDCOM, default='')
    cpu_brand = models.CharField(max_length=10, verbose_name='ยี่ห้อของ CPU')
    # cpu_model = models.CharField(max_length=10, verbose_name='รุ่นของ CPU', choices=CHOICES_BRANDCPU, default='')
    cpu_model = models.CharField(max_length=20, verbose_name='รุ่นของ CPU')
    cpu_speed_clock = models.CharField(max_length=5, verbose_name='ความเร็วสัญญาณนาฬิกา')
    cpu_unit_speed_clock = models.CharField(max_length=3, verbose_name='หน่วยความเร็วสัญญาณนาฬิกา')
    computer_mac_address = models.CharField(max_length=17, verbose_name='MAC Address')
    computer_use_network = models.CharField(max_length=20, verbose_name='เครื่องข่ายที่ใช้')
    ram_type = models.CharField(max_length=5, verbose_name='RAM')
    ram_capacity = models.CharField(max_length=3, verbose_name='ความจุ RAM')
    ram_unit_capacity = models.CharField(max_length=3, verbose_name='หน่วย RAM')
    harddisk_type_1 = models.CharField(max_length=10, verbose_name='ประเภท Harddisk ')
    harddisk_capacity_1 = models.CharField(max_length=5, verbose_name='ความจุของ Harddisk Primary')
    harddisk_unit_1 = models.CharField(max_length=5, verbose_name='หน่วย Harddisk Primary')
    harddisk_type_2 = models.CharField(max_length=10, verbose_name='ประเภท Harddisk Primary')
    harddisk_capacity_2 = models.CharField(max_length=5, verbose_name='ความจุของ Harddisk Secondary')
    harddisk_unit_2 = models.CharField(max_length=5, verbose_name='หน่วย Harddisk Secondary')
    os_computer = models.CharField(max_length=20, verbose_name='ชื่อระบบปฏิบัติการ Secondary')
    os_copyright = models.CharField(max_length=5, verbose_name='ลิขสิทธิ์ของระบบปฏิบัติการ')
    office_name = models.CharField(max_length=50, verbose_name='ชื่อโปรแกรมสำนักงาน')
    office_model_year = models.CharField(max_length=4, verbose_name='รุ่นโปรแกรม')
    office_copyright = models.CharField(max_length=5, verbose_name='ลิขสิทธิ์ของโปรแกรมสำนักงาน')
    antivirus_name = models.CharField(max_length=50, verbose_name='ชื่อโปรแกรมป้องกันไวรัส')
    antivirus_copyright = models.CharField(max_length=5, verbose_name='ลิขสิทธิ์ของโปรแกรม')
    computer_acquisition = models.CharField(max_length=50, verbose_name='คอมพิวเตอร์จากโครงการ')
    computer_start_use_year = models.CharField(max_length=4, verbose_name='เริ่มใช้เครื่อง พ.ศ.?')
    # computer_end_use_year = models.CharField(max_length=10, verbose_name='ประเภท Harddisk')
    person_responsible = models.CharField(max_length=100, verbose_name='ผู้รับผิดชอบ')
    person_responsible_phone = models.CharField(max_length=10, verbose_name='เบอร์ติดต่อผู้รับผิดชอบ')
    # status_computer = models.CharField(max_length=20, verbose_name='รุ่นของ CPU', choices=CHOICES_STATUSCOM, default='ใช้ราชการ')
    status_computer = models.CharField(max_length=20, verbose_name='สถานภาพ Computer')
    note = models.CharField(max_length=100, verbose_name=' หมายเหตุ',  blank=True)
    created_by = models.ForeignKey(User, related_name='computers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.computer_install_place +' '+ self.person_responsible + ' '+ self.person_responsible_phone
        # +' '+self.status_computer

    # mouse_brand = models
    # mouse_serial = models
    # mouse_type_wired = models
    # computer_note = models
    # keyboard_brand = models
    # keyboard_serial = models
    # keyboard_type_wired = models
    # computer_note = models
    # created_by = models.ForeignKey(User, related_name='updatenotes', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)


class Upgradecomputer(models.Model):

    NOTEBOOK = 'notbook'
    PC = 'pc'
    PCSERVER = 'pcserver'

    CHOICES_TYPECOM = (
        (NOTEBOOK, 'notebook'),
        (PC, 'pc'),
        (PCSERVER, 'pc server'),
    )

    HANDMAKE = 'handmake'
    ACER = 'acer'
    HP = 'hp'
    Lenovo = 'lenovo'
    SVOA = 'svoa' 


    CHOICES_BRANDCOM = (

        (HANDMAKE, 'Handmake'),
        (ACER, 'Acer'),
        (HP, 'Hp'),
        (Lenovo, 'Lenovo'),
        (SVOA, 'SVOA'),
    )
    
    AMD = 'AMD'
    INTEL = 'INTEL'
    other = 'Other'


    CHOICES_BRANDCPU = (

        (AMD, 'AMD'),
        (INTEL, 'INTEL'),
        (INTEL, 'Other'),

    )

    ACTIVE = 'ใช้ราชการ'
    INACTIVE = 'ชำรุด'
    MANTAINENT = 'ส่งซ่อม'
    CHANGE = 'เบิกเปลี่ยน'
    SENTBACK = 'ส่งคืน'


    CHOICES_STATUSCOM = (

        (ACTIVE,'ใช้ราชการ'),
        (INACTIVE, 'ชำรุด'),
        (MANTAINENT, 'ส่งซ่อม'),
        (CHANGE, 'เบิกเปลี่ยน'),
        (SENTBACK, 'ส่งคืน'),

    )



    team_name = models.ForeignKey(Team, related_name='upgradecomputers', on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, related_name='upgradecomputers', on_delete=models.CASCADE)
    computer_upgrade_year = models.CharField(max_length=4, verbose_name = "ปี พ.ศ.upgrade อุปกรณ์")
    computer_install_place = models.CharField(max_length=100, verbose_name = "สถานที่ติดตั้งอุปกรณ์")
    computer_name = models.CharField(max_length=100, verbose_name='ชื่อเครื่องคอมพิวเตอร์')
    cpu_brand = models.CharField(max_length=10, verbose_name='ยี่ห้อของ CPU')
    cpu_model = models.CharField(max_length=20, verbose_name='รุ่นของ CPU')
    cpu_speed_clock = models.CharField(max_length=5, verbose_name='ความเร็วสัญญาณนาฬิกา')
    cpu_unit_speed_clock = models.CharField(max_length=3, verbose_name='หน่วยความเร็วสัญญาณนาฬิกา')
    computer_use_network = models.CharField(max_length=20, verbose_name='เครื่องข่ายที่ใช้')
    ram_type = models.CharField(max_length=5, verbose_name='RAM')
    ram_capacity = models.CharField(max_length=3, verbose_name='ความจุ RAM')
    ram_unit_capacity = models.CharField(max_length=3, verbose_name='หน่วย RAM')
    harddisk_type_1 = models.CharField(max_length=10, verbose_name='ประเภท Harddisk')
    harddisk_capacity_1 = models.CharField(max_length=5, verbose_name='ความจุของ Harddisk')
    harddisk_unit_1 = models.CharField(max_length=5, verbose_name='หน่วย Harddisk')
    harddisk_type_2 = models.CharField(max_length=10, verbose_name='ประเภท Harddisk')
    harddisk_capacity_2 = models.CharField(max_length=5, verbose_name='ความจุของ Harddisk')
    harddisk_unit_2 = models.CharField(max_length=5, verbose_name='หน่วย Harddisk')
    os_computer = models.CharField(max_length=20, verbose_name='ชื่อระบบปฏิบัติการ')
    os_copyright = models.CharField(max_length=5, verbose_name='ลิขสิทธิ์ของระบบปฏิบัติการ')
    office_name = models.CharField(max_length=50, verbose_name='ชื่อโปรแกรมสำนักงาน')
    office_model_year = models.CharField(max_length=4, verbose_name='รุ่นโปรแกรม')
    office_copyright = models.CharField(max_length=5, verbose_name='ลิขสิทธิ์ของโปรแกรมสำนักงาน')
    antivirus_name = models.CharField(max_length=50, verbose_name='ชื่อโปรแกรมป้องกันไวรัส')
    antivirus_copyright = models.CharField(max_length=5, verbose_name='ลิขสิทธิ์ของโปรแกรม')
    person_responsible = models.CharField(max_length=100, verbose_name='ผู้รับผิดชอบ',  blank=True)
    person_responsible_phone = models.CharField(max_length=10, verbose_name='ประเภท Harddisk', blank=True)
    status_computer = models.CharField(max_length=20, verbose_name='สถานภาพ Computer')
    note = models.CharField(max_length=100, verbose_name=' หมายเหตุ',  blank=True)
    created_by = models.ForeignKey(User, related_name='upgradecomputers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.computer.computer_install_place +' '+ self.computer_upgrade_year 
        # +' '+self.status_computer