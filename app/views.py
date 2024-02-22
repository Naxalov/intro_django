from django.http import HttpRequest, JsonResponse, HttpResponse
from .models import Person

    
def index(request: HttpRequest):
    return JsonResponse({'message': 'Hello, World!'})

def about(request: HttpRequest):
    return JsonResponse({'message': 'About Page'})

def home(request: HttpRequest,pk=0):
    x = Person.objects.all()
    # print type of x
    for p in x:
        print(p.first_name)
    
    print('Get request')
    return JsonResponse({'message': f'Welcome to the API!: {pk}'})