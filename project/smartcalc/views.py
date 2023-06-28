from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .services import services


def index(request):  # return value and oaram type
    """Главная страница. Веб-сервис, выполняющий вычисление выражения"""

    data: dict = {'history': services.read_history()}

    if request.method == 'POST':

        if 'clean_history' in request.POST:
            data['history'] = services.clean_history()
            return render(request, "index.html", data)

        elif 'equal' in request.POST:
            if request.POST.get('expression') == '' or request.POST.get('x_num') == '':
                return render(request, "index.html", {'result': 'Please, enter an expression'})
            else:
                result: str = services.get_expression_result(request.POST.get('expression'), request.POST.get('x_num'))
                data['history'] = services.write_history(request.POST.get('expression'), request.POST.get(
                    'x_num'))  # запишем только если посчиталось без ошибок или всегда ???
                data['result'] = result
                return render(request, "index.html", data)

    return render(request, "index.html", data)


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
