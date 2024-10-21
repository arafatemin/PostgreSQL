from django.shortcuts import render

from .models import *

def index(request):
    context = {
        'persons': Person.objects.all()
    }
    return render(request, 'sql/index.html', context)

