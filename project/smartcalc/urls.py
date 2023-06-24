from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('settings/', views.settings, name='settings'),
    path('graph/', views.graph, name='graph'),
    path('about/', views.about, name='about'),
    path('calculate', views.get_expression_result, name='calculate'),
    path('graph', views.graph_expression, name='graph'),
]
