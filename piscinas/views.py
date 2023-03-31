from django.shortcuts import render
import services
from .models import *

# Create your views here.
def index(request):
    template = "lagunas.html"

    data = dict()

    lagunas = Laguna.objects.all()

    data["lagunas"] = lagunas

    return render(request, template, data)

def detalleLagunas(request, pk):
    template = "detalleLagunas.html"

    data = dict()

    laguna = Laguna.objects.get(pk=pk)

    aireadores = Aireador.objects.filter(laguna=laguna)

    data["laguna"] = laguna
    data["aireadores"] = aireadores

    return render(request, template, data)

def indexprincipal(request):
    template = "index.html"

    data = dict()

    return render(request, template, data)

def indexprincipal2(request):
    template = "index2.html"

    data = dict()

    return render(request, template, data)

def arduino(request):
    template = "arduino.html"

    data = dict()

    params = {  }

    response = services.generate_request('https://api.thingspeak.com/channels/1886466/feeds.json?api_key=PIEDQMTON7ELAUFE', params)

    data["response"] = response

    temperatura = list()
    humedad = list()
    fechas = list()
    ids = list()

    for medicion in response["feeds"]:
        fechas.append(medicion["created_at"][0:10] + " - " + medicion["created_at"][-9:-1])
        ids.append(str(medicion["entry_id"]))

        if(medicion["field1"] is not None):
            humedad.append(float(medicion["field1"]))
        else:
            humedad.append(0)

        if(medicion["field2"] is not None):
            temperatura.append(float(medicion["field2"]))
        else:
            temperatura.append(0)

    data["fechas"] = fechas
    data["humedad"] = humedad
    data["temperatura"] = temperatura
    data["ids"] = ids
    

    return render(request, template, data)