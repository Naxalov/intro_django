from django.contrib import admin
from django.urls import path,include
from app.views import index, home, get_all_items


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('app/',include('app.urls')),


]
