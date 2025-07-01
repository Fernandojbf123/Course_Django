from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def primera_vista(request):
    return HttpResponse('Esta es mi primera vista. Recuerda que las vistas son ese punto de intermedio que recibe la interacción del HTML y lo envía al modelo')