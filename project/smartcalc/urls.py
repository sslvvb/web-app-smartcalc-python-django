from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('graph/', views.graph, name='graph'),
    path("about/", TemplateView.as_view(template_name="about.html")),
]
