from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Device

def dashboard(request):
    """首页仪表盘"""
    total = Device.objects.count()
    online = Device.objects.filter(status='online').count()
    return render(request, 'dashboard.html', {
        'total': total,
        'online': online,
    })

def device_list(request):
    """设备列表页"""
    devices = Device.objects.all()
    return render(request, 'device_list.html', {'devices': devices})
