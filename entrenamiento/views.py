from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers
from django.http import Http404, HttpResponseNotAllowed
from .models import Entrenamiento, Ejercicio, Serie
import json

# Create your views here.

TDE = "Training does not exist"

def start(request):
    html = '''
    <html>
        <body>
            <h1>Hello from Gym-app!</h1>
        </body>
    </html>
    '''
    return HttpResponse(html)


# Create something
def create_new_training(request): 
    print(request)   
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        new_fecha = body.get("fecha")
        new_duracion = body.get("duracion")
        new_calorias = body.get("calorias")
        
        new_trainning = Entrenamiento(fecha=new_fecha, duracion=new_duracion, calorias=new_calorias)
        new_trainning.save()
        return HttpResponse(status=200)
    else:
        raise HttpResponseNotAllowed("Method is not supported")

# Get All
def get_all_trainings(request):
    if request.method == 'GET':
        trainings = Entrenamiento.objects.all()
        data = serializers.serialize('json', trainings)
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponseNotAllowed(['GET'])
    
# Get by ID
def get_training_by_id(request, training_id):
    if request.method == 'GET':
        try:
            training = Entrenamiento.objects.get(entrenamiento_id=training_id)
            data = serializers.serialize('json', [training])
            return HttpResponse(data, content_type='application/json')
        except Entrenamiento.DoesNotExist:
            raise Http404(TDE)
    else:
        return HttpResponseNotAllowed(['GET'])

# Update by ID
def update_training_by_id(request, training_id):
    if request.method == 'PATCH':
        try:
            training = Entrenamiento.objects.get(entrenamiento_id=training_id)
            data = json.loads(request.body)
            if 'fecha' in data:
                training.fecha = data['fecha']
            if 'duracion' in data:
                training.duracion = data['duracion']
            if 'calorias' in data:
                training.calorias = data['calorias']
            training.save()
            return HttpResponse("Training updated")
        except Entrenamiento.DoesNotExist:
            raise Http404(TDE)
    else:
        return HttpResponseNotAllowed(['PATCH'])

# Delete by ID 
def delete_training_by_id(request, training_id):
    if request.method == 'DELETE':
        try:
            training = Entrenamiento.objects.get(entrenamiento_id=training_id)
            training.delete()
            return HttpResponse("Training deleted")
        except Entrenamiento.DoesNotExist:
            raise Http404(TDE)
    else:
        return HttpResponseNotAllowed(['DELETE'])
    
    