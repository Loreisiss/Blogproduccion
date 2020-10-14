from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='homes'),
    
    path('generales/',generales,name='general'),
    path('programacion/',programa,name='progra'),
    path('contacto/',contacto,name='contac'),
    path('<slug:slug>/',detallespost,name='detalle_post'),
]