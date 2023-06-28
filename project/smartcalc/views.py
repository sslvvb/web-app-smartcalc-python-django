from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .services import services


def index(request):
    """Главная страница. Веб-сервис, выполняющий вычисление выражения"""
    if request.method == 'POST':
        if request.POST.get('expression') == '' or request.POST.get('x_num') == '':
            return render(request, "index.html", {'result': 'Please, enter an expression'})
        result: str = services.get_expression_result(request.POST.get('expression'), request.POST.get('x_num'))
        return render(request, "index.html", {'result': result})
    else:
        return render(request, "index.html")


def settings(request):
    return render(request, "settings.html")


def graph_expression(request):
    """Веб-сервис, выполняющий отрисовку графика выражения"""
    if request.method == 'POST':
        expression = request.POST.get('expression')
        # Generate the chart based on the expression
        # You can use libraries like matplotlib or Chart.js to create the chart
        return render(request, 'graph.html')
    else:
        return HttpResponse(status=400)


def about(request):
    return render(request, "about.html")


def page_not_found(request, exception):
    # сюда добавить красивую страничку для 404
    return HttpResponseNotFound("sslvvb Страница не найдена")
