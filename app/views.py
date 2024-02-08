from django.http import HttpRequest, JsonResponse
import json
data = {
    1: {
        'name': 'Milk',
        'price': 2.5,
        'quantity': 10
    },
    2: {
        'name': 'Bread',
        'price': 1.5,
        'quantity': 20
    },
}
# Grocery store API
# GET /items/ - Get all items
# POST /items/ - Add a new item
# GET /items/<id>/ - Get item by id


def get_all_items(request: HttpRequest):
    return JsonResponse(data)

def index(request: HttpRequest):

    print(request.scheme)
    # Get query parameters

    a = request.GET.get('a', '0')   # default value is '0'
    b = request.GET.get('b', '0')   # default value is '0'
    data = {
        'a': a,
        'b': b
    }
    # Get json request body
    if request.method == 'POST':
        data = request.POST
        body = request.body
        # Convert bytes to string
        # body = body.decode('utf-8')
        # Convert string to dictionary
        data = json.loads(body)
        print(data['a'])

    return JsonResponse(data)
def home(request: HttpRequest):
    return JsonResponse({'message': 'Welcome to the API!'})