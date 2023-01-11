from django.contrib.auth.models import User
from django.db import models

class Personal(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'In Active'),
    )

    # team = models.ForeignKey(Team, verbose_name = "สังกัด", related_name='leads', on_delete=models.CASCADE)
    rank = models.CharField(verbose_name = "ยศ", max_length=10)
    first_name = models.CharField(verbose_name = "ชื่อ", max_length=50)
    last_name = models.CharField(verbose_name = "นามสกุล", max_length=50)
    position = models.CharField(verbose_name = "ตำแหน่ง", max_length=100)
    email_rtaf = models.EmailField(verbose_name = "@rtaf")
    email_public = models.EmailField(verbose_name = "@gmail")
    mobile = models.CharField(verbose_name = "เบอร์โทรศัพท์เคลื่อนที่", max_length=10,  blank=True)
    phone_rtaf = models.CharField(verbose_name = "เบอร์โทรภายใน ทอ.", max_length=5)
    department = models.CharField(max_length=100, verbose_name="สังกัด", default = "-", blank=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    created_by = models.ForeignKey(User, related_name='personals', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rank+' '+ self.first_name +' '+ self.last_name +' '+self.department