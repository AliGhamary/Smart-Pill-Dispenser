from django.shortcuts import render
from .models import Pill

# Create your views here.
def home(request):
    pills = Pill.objects.all()
    pill1 = pills.filter(pk = 1).first()
    pill2 = pills.filter(pk = 2).first()
    pill3 = pills.filter(pk = 3).first()
    pill4 = pills.filter(pk = 4).first()

    context = {
        "pills": pills,
        "pill1": pill1,
        "pill2": pill2,
        "pill3": pill3,
        "pill4": pill4,
    }

    return render(request, 'home/index.html', context)


def container(request):
    return render(request, 'home/container.html')