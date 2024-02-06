from django.http import HttpResponse,HttpRequest,JsonResponse
from django.urls import path

def index(request: HttpRequest):
    # Get query parameters
    a = request.GET.get('a', '0')   # default value is '0'
    b = request.GET.get('b', '0')   # default value is '0'
    data = {
        'a': a,
        'b': b
    }
    return JsonResponse(data)

 
urlpatterns = [
    
    path('',index),

]
