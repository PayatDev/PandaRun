from django.db import models
from datetime import datetime

# Create your models here.
class full_runner(models.Model):
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)

    age = models.IntegerField(default=None)

    GENDER = (
        ('M', 'ชาย'),
        ('F', 'หญิง'),
    )
    gender = models.CharField(max_length=1, choices=GENDER, default=None)

    SHIRT_SIZES = (
        ('3S', '3S ขนาดรอบอก 32 นิ้ว'),
        ('2S', '2S ขนาดรอบอก 34 นิ้ว'),
        ('S', 'S ขนาดรอบอก 36 นิ้ว'),
        ('M', 'M ขนาดรอบอก 38 นิ้ว'),
        ('L', 'L ขนาดรอบอก 40 นิ้ว'),
        ('XL', 'XL ขนาดรอบอก 42 นิ้ว'),
        ('2XL', '2XL ขนาดรอบอก 44 นิ้ว'),
        ('3XL', '3XL ขนาดรอบอก 46 นิ้ว'),
        ('4XL', '4XL ขนาดรอบอก 48 นิ้ว'),
    )
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES, default=None)

    team = models.CharField(max_length=50, default=None)

    address = models.CharField(max_length=250, default=None)

    mobile = models.CharField(max_length=10, default=None)

    SEND = (
        ('EVENT', 'รับหน้างาน'),
        ('EMS', 'ส่ง EMS')
    )
    send = models.CharField(max_length=5, choices=SEND, default=None)

    STATUS = (
        ('รอตรวจสอบ', 'Pending'),
        ('ลงทะเบียนสำเร็จ', 'Approved'),
        ('มีปัญหา', 'Problem'),
    )
    status = models.CharField(max_length=20, choices=STATUS, default='รอตรวจสอบ')

    capture = models.FileField(upload_to='slip/', default=None)

    def __str__(self):
        return self.first_name + " " + self.last_name

class half_runner(models.Model):
    first_name = models.CharField(max_length=50, default=None)
    last_name = models.CharField(max_length=50, default=None)

    age = models.IntegerField(default=None)

    GENDER = (
        ('M', 'ชาย'),
        ('F', 'หญิง'),
    )
    gender = models.CharField(max_length=1, choices=GENDER, default=None)

    SHIRT_SIZES = (
        ('3S', '3S ขนาดรอบอก 32 นิ้ว'),
        ('2S', '2S ขนาดรอบอก 34 นิ้ว'),
        ('S', 'S ขนาดรอบอก 36 นิ้ว'),
        ('M', 'M ขนาดรอบอก 38 นิ้ว'),
        ('L', 'L ขนาดรอบอก 40 นิ้ว'),
        ('XL', 'XL ขนาดรอบอก 42 นิ้ว'),
        ('2XL', '2XL ขนาดรอบอก 44 นิ้ว'),
        ('3XL', '3XL ขนาดรอบอก 46 นิ้ว'),
        ('4XL', '4XL ขนาดรอบอก 48 นิ้ว'),
    )
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES, default=None)

    team = models.CharField(max_length=50, default=None)

    address = models.CharField(max_length=250, default=None)

    mobile = models.CharField(max_length=10, default=None)

    SEND = (
        ('EVENT', 'รับหน้างาน'),
        ('EMS', 'ส่ง EMS')
    )
    send = models.CharField(max_length=5, choices=SEND, default=None)

    STATUS = (
        ('รอตรวจสอบ', 'Pending'),
        ('ลงทะเบียนสำเร็จ', 'Approved'),
        ('มีปัญหา', 'Problem'),
    )
    status = models.CharField(max_length=20, choices=STATUS, default='รอตรวจสอบ')

    capture = models.FileField(upload_to='slip/', default=None)

    def __str__(self):
        return self.first_name + " " + self.last_name

class contact(models.Model):
    first_name = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    mobile = models.CharField(max_length=10, default=None)
    comment = models.TextField(max_length=500, default=None)

    def __str__(self):
        return self.first_name
