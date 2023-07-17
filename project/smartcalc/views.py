from django.shortcuts import render
from .services import services
import logging
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

logger = logging.getLogger(__name__)


def index(request):
    """Веб-сервис, выполняющий вычисление выражения"""
    config: dict = services.read_config()

    data: dict = {'history': services.read_history(),
                  'background': config['background'],
                  'font_size': config['font_size'],
                  'main_color': config['main_color']}

    if request.method == 'POST':
        # elif 'select' in request.POST:
        #     history_item: str = request.POST.get('history')
        #     if history_item:
        #         history_item = history_item.rstrip()
        #         split_lines: list = history_item.split('=')
        #         data['expression_or_result'] = split_lines[0]
        #         data['x_value'] = split_lines[2]
        #         data['history'] = services.write_history(history_item)

        if 'equal' in request.POST:
            expression: str = request.POST.get('expression')
            x_value: str = request.POST.get('x_num')
            result: str = services.get_expression_result(expression, x_value)
            if result != "Error in expression":
                data['history'] = services.write_history(f'{expression}={result}; x={x_value}')
            logger.info(f'{expression}={result}; x={x_value}')  # TODO: log
            data['expression_or_result'] = result

    return render(request, "index.html", data)


def clean_history(request):
    if request.method == 'POST':
        services.clean_history()
        logger.info('Clean history file.')
    return HttpResponseRedirect("/")


def change_background(request):
    return _change_config(request, 'background', 'Change background')


def change_main_color(request):
    return _change_config(request, 'main_color', 'Change main accent color')


def change_font_size(request):
    return _change_config(request, 'font_size', 'Change font size')


def _change_config(request, setting_name, log_message):
    if request.method == 'POST':
        setting_value = request.POST.get(setting_name)
        if services.update_config(setting_name, setting_value):
            logger.info(f'{log_message} to {setting_value}')
        else:
            logger.warning(f'Failed to {log_message} to {setting_value}')
    return HttpResponseRedirect("/")


# TODO: log
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


# TODO: log ???
def about(request):
    config: dict = services.read_config()
    data: dict = {'background': config['background'],
                  'font_size': config['font_size'],
                  'main_color': config['main_color']}
    return render(request, "about.html", data)

# def page_not_found(request, exception):
#     # сюда добавить красивую страничку для 404
#     return HttpResponseNotFound("sslvvb Страница не найдена")
