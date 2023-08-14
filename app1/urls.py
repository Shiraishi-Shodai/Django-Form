from .views import *
from django.urls import path

app_name = 'app1'

urlpatterns = [
    path('', index, name='index'),
    path('modelput/', modelPut, name='modelPut')
]
