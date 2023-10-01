"""Django views for the SmartCalc application."""

from django.shortcuts import render, redirect
from .services import services
import logging
import math

logger = logging.getLogger(__name__)


def index(request):
    data: dict = _collect_basic_data()

    if request.method == 'POST':
        if 'equal' in request.POST:
            expression: str = request.POST.get('expression')
            x_value: str = request.POST.get('x_num')
            result: str = services.get_expression_result(expression, x_value)
            if result != 'Error in expression':
                data['history'] = services.write_history(
                    f'{expression}={result}; x={x_value}')
            logger.info('%s=%s; x=%s', expression, result, x_value)
            data['expression_or_result'] = result
            data['x_value'] = x_value

    return render(request, 'index.html', data)


def clean_history(request):
    if request.method == 'POST':
        services.clean_history()
        logger.info('Clean history file.')
    return redirect('index')


def change_background(request):
    return _change_config(request, 'background', 'Change background')


def change_main_color(request):
    return _change_config(request, 'main_color', 'Change main accent color')


def change_font_size(request):
    return _change_config(request, 'font_size', 'Change font size')


def graph(request):
    data: dict = _collect_basic_data()
    if request.method == 'POST':
        expression = request.POST.get('expression')
        data['expression'] = expression
        data['x_min'] = request.POST.get('x_min')
        data['x_max'] = request.POST.get('x_max')
        data['y_min'] = request.POST.get('y_min')
        data['y_max'] = request.POST.get('y_max')
        result: list = services.calculate_graph_expression_result(
            data['expression'], data['x_min'], data['x_max'])

        if result is None:
            data['expression'] = 'Error in expression'
            logger.warning('Error in expression for graph: %s', expression)
        else:
            x_values, y_values = result[0], result[1]

            valid_indices = [
                i for i in range(len(x_values)) if
                not (math.isnan(x_values[i]) or math.isnan(y_values[i]))
            ]
            x_values = [x_values[i] for i in valid_indices]
            y_values = [y_values[i] for i in valid_indices]

            xy_values: list = [{'x': x, 'y': y} for x, y in
                               zip(x_values, y_values)]
            data['xy_values'] = xy_values
            logger.info('Print graph for: %s', expression)
    return render(request, 'graph.html', data)


def about(request):
    data: dict = _collect_basic_data()
    logger.info('Visit the About page')
    return render(request, 'about.html', data)


def _collect_basic_data() -> dict:
    config: dict = services.read_config()
    data: dict = {'history': services.read_history(),
                  'background': config['background'],
                  'font_size': config['font_size'],
                  'main_color': config['main_color']}
    return data


def _change_config(request, setting_name, log_message):
    if request.method == 'POST':
        setting_value = request.POST.get(setting_name)
        if services.update_config(setting_name, setting_value):
            logger.info('%s to %s.', log_message, setting_value)
        else:
            logger.warning('Failed to %s to %s.', log_message, setting_value)
    return redirect('index')
