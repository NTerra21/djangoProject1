from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template, Context, loader

def inicio(request):
    plantilla = loader.get_template('plantilla.html')

    variables = {
        "dato1": "Hola Mundo",
        "fecha": datetime.now()
    }

    contexto = Context(variables)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

def curso(request, nombre, camada):
    contexto = {
        'nombres': {
            'Nombre1': 'Nicolas',
            'Nombre2': 'Maximo',
            'Nombre3': 'Gasparin',

        }
    }
    return render(request, 'cursos.html', contexto)