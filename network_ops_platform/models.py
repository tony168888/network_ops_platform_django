from django.db import models

# Create your models here.
from django.db import models

class Device(models.Model):
    STATUS_CHOICES = [
        ('online', '在线'),
        ('offline', '离线'),
    ]
    name = models.CharField(max_length=100, verbose_name='设备名称')
    ip = models.GenericIPAddressField(verbose_name='管理IP')
    vendor = models.CharField(max_length=50, verbose_name='厂商')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='offline')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备'

    def __str__(self):
        return f"{self.name} ({self.ip})"
