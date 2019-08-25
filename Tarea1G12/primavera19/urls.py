from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('inputs/', inputs, name='inputs'),
	path('inicio/', inicio, name='inicio'),
	path('contacto/', contacto, name='contacto')
]