from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    contenido = {'nombre_sitio': "LibrosOnline"}
    return render(request, 'vistaprevia/index.html', contenido)
    # return HttpResponse("Hola Mundo!.")


# Create your views here.
