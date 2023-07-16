from django.shortcuts import render
from .services import services
import logging
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

logger = logging.getLogger(__name__)

config: dict = services.read_config()

data: dict = {'history': services.read_history(),
              'background': config['background'],
              'font_size': config['font_size'],
              'main_color': config['main_color']}


def index(request):  # return value and param type
    """Главная страница. Веб-сервис, выполняющий вычисление выражения"""

    if request.method == 'POST':
        expression: str = request.POST.get('expression')
        x_value: str = request.POST.get('x_num')

        if 'clean_history' in request.POST:
            data['history'] = services.clean_history()
            logger.info('Clean history file.')

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
            logger.info(f'{expression}={result}; x={x_value}')  # TODO
            data['expression_or_result'] = result

        elif 'select-background' in request.POST:
            config = services.write_background_to_config(request.POST.get('background'))
            data['background'] = config['background']

        elif 'select-main-color' in request.POST:
            config = services.write_main_color_to_config(request.POST.get('main_color'))
            data['main_color'] = config['main_color']

        elif 'select-font-size' in request.POST:
            config = services.write_font_size_to_config(request.POST.get('font_size'))
            data['font_size'] = config['font_size']

    return render(request, "index.html", data)


def history(request):
    if request.method == 'POST':
        history_item: str = request.POST.get('history')
        if history_item:
            history_item = history_item.rstrip()
            split_lines: list = history_item.split('=')
            data['expression_or_result'] = split_lines[0]
            data['x_value'] = split_lines[2]
            data['history'] = services.write_history(history_item)

    return HttpResponseRedirect("/")


def graph(request):
    """Веб-сервис, выполняющий отрисовку графика выражения"""
    if request.method == 'POST':
        expression = request.POST.get('expression')
        x_min = request.POST.get('x_min')
        x_max = request.POST.get('x_max')
        y_min = request.POST.get('y_min')
        y_max = request.POST.get('y_max')

        result: list = services.graph_expression_result(expression, x_min, x_max)  # get or calc ?
        xy_values: list = [{'x': x, 'y': y} for x, y in zip(result[0], result[1])]

        data: dict = {'expression': expression,
                      'xy_values': xy_values,
                      'x_min': float(x_min),
                      'x_max': float(x_max),
                      'y_min': float(y_min),
                      'y_max': float(y_max)
                      }
        return render(request, 'graph.html', data)
    # else:
    #     return HttpResponse(status=400)  # change to /


def about(request):
    config: dict = services.read_config()
    print(config)

    # мб перенести вниз чтобы каждый раз потом не делать заполнение ?
    # мб избавиться когда появятся стили ???
    data: dict = {'background': config['background'],
                  'font_size': config['font_size'],
                  'main_color': config['main_color']}

    return render(request, "about.html", data)

# def page_not_found(request, exception):
#     # сюда добавить красивую страничку для 404
#     return HttpResponseNotFound("sslvvb Страница не найдена")
