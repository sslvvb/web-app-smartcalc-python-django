# Центральным моментом любого веб-приложения является обработка запроса, который отправляет пользователь.
# В Django за обработку запроса отвечают представления или views.
# По сути представления представляют функции обработки, которые принимают данные запроса в
# виде объекта HttpRequest из пакета django.http и генерируют некоторый результат,
# который затем отправляется пользователю.

# представлены функции, которые будут обрабатывать запросы
# связь функций с запросами


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def settings(request):
    return render(request, "settings.html")


def graph(request):
    return render(request, "graph.html")


def about(request):
    return render(request, "about.html")
