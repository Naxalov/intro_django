from django.http import HttpRequest, JsonResponse, HttpResponse
from .models import Person

    
def index(request: HttpRequest):
    return JsonResponse({'message': 'Hello, World!'})

def about(request: HttpRequest):
    return JsonResponse({'message': 'About Page'})

def home(request: HttpRequest,pk=0):
    return JsonResponse({'message': f'Welcome to the API!: {pk}'})