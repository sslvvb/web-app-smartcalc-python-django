from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('settings/', settings, name='settings'),
    path('graph/', graph, name='graph'),
    path('about/', about, name='about'),
    # path('calculate', calculate_expression, name='calculate'),
    path('calculate', calculate_expression, name='calculate'),
    path('graph', graph_expression, name='graph'),
]
