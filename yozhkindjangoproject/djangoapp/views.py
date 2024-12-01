from django.shortcuts import render
from .models import *

def data_table(request):
    brigades = Brigades.objects.all()
    workers = Workers.objects.select_related('number_brigade').all()
    locomotives = Locomotives.objects.all()
    repairs = Repairs.objects.select_related('reg_num_loc','number_brigade').all()
    data = {
        'brigades': brigades,
        'workers': workers,
        'locomotives': locomotives,
        'repairs': repairs
    }
    return render(request, 'index.html',data)