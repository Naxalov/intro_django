from django.urls import path
from .views import index,home,about
urlpatterns = [
    

    path('home/<int:pk>/', home),
    path('home/', home),
    path('index/', index),
    path('index/about', about),



]
