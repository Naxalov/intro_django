from django.http import HttpRequest, JsonResponse, HttpResponse
from .models import Person
import json

    
def index(request: HttpRequest):
    return JsonResponse({'message': 'Hello, World!'})

def about(request: HttpRequest):
    return JsonResponse({'message': 'About Page'})

def home(request: HttpRequest,pk=0):
    if request.method=='POST':
        data = request.body.decode('utf-8')
        # convert string to dictionary
        data = json.loads(data)
        first_name = data['first_name']
        last_name = data['last_name']
        job = data['job']
        person = Person.objects.create(
            first_name=first_name,
            last_name=last_name,
            job=job,
            count=0
        
        )
    else:
        return JsonResponse({'message':'josn'})

   
   
    return JsonResponse({'message': 'User Created successfully'})