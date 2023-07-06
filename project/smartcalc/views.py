from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .services import services
import json


def index(request):  # return value and param type
    """Главная страница. Веб-сервис, выполняющий вычисление выражения"""

    data: dict = {'history': services.read_history()}  # мб перенести вниз чтобы каждый раз потом не делать заполнение ?

    if request.method == 'POST':
        expression: str = request.POST.get('expression')
        x_value: str = request.POST.get('x_num')

        if 'clean_history' in request.POST:
            data['history'] = services.clean_history()

        elif 'select' in request.POST:
            history_item: str = request.POST.get('history')
            if history_item:
                history_item = history_item.rstrip()
                split_lines: list = history_item.split('=')
                data['expression_or_result'] = split_lines[0]
                data['x_value'] = split_lines[2]
                data['history'] = services.write_history(history_item)

        elif 'equal' in request.POST:
            result: str = services.get_expression_result(expression, x_value)
            if result != "Error in expression":
                data['history'] = services.write_history(f'{expression}={result}; x={x_value}')
            data['expression_or_result'] = result

    return render(request, "index.html", data)


# TODO: график починить и отрисовать красиво
def graph(request):
    """Веб-сервис, выполняющий отрисовку графика выражения"""
    if request.method == 'POST':
        expression = request.POST.get('expression')
        x_min = request.POST.get('x_min')
        x_max = request.POST.get('x_max')
        y_min = request.POST.get('y_min')
        y_max = request.POST.get('y_max')

        result: list = services.graph_expression_result(expression, x_min, x_max)  # get or calc ?

        data_json = json.dumps(result)

        data: dict = {'data': data_json}

        return render(request, 'graph.html', data)
    # else:
    #     return HttpResponse(status=400)  # change to /


def page_not_found(request, exception):
    # сюда добавить красивую страничку для 404
    return HttpResponseNotFound("sslvvb Страница не найдена")
