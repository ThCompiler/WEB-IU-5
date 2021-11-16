from django.shortcuts import render
from main.models import Icecreams, Company


# Create your views here.


def index(request):
    return render(request, 'master.html', {'icecreams': Icecreams.objects.get_short_des()})


def icecream(request, pk):
    return render(request, 'details.html', {'icecream': Icecreams.objects.get_current(pk)})
