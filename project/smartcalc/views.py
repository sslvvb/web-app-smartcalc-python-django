from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .services import services


def index(request):  # return value and oaram type
    """Главная страница. Веб-сервис, выполняющий вычисление выражения"""

    data: dict = {'history': services.read_history()}

    if request.method == 'POST':
        expression: str = request.POST.get('expression')
        x_num: str = request.POST.get('x_num')

        if 'clean_history' in request.POST:
            data['history'] = services.clean_history()

        elif 'select' in request.POST:
            history_item: str = request.POST.get('history').rstrip()
            split_lines: list = history_item.split('=')
            data['expression_or_result'] = split_lines[0]
            data['x_value'] = split_lines[2]
            data['history'] = services.write_history(history_item)

        elif 'equal' in request.POST:
            if expression == '' or x_num == '':
                data['expression_or_result'] = 'Please, enter an expression'
            else:
                result: str = services.get_expression_result(expression, x_num)
                data['history'] = services.write_history(f'{expression}={result}; x={x_num}')  # только если без ошибок
                data['expression_or_result'] = result

    return render(request, "index.html", data)  # могу возвращать не словарик, а объект класса - см метанит


def graph(request):
    """Веб-сервис, выполняющий отрисовку графика выражения"""
    if request.method == 'POST':
        expression = request.POST.get('expression')
        # Generate the chart based on the expression
        # You can use libraries like matplotlib or Chart.js to create the chart
        return render(request, 'graph.html')
    else:
        return HttpResponse(status=400)


def page_not_found(request, exception):
    # сюда добавить красивую страничку для 404
    return HttpResponseNotFound("sslvvb Страница не найдена")
