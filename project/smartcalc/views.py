from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .services import services


def index(request):
    """Main application page"""
    return render(request, "index.html")


def settings(request):
    return render(request, "settings.html")


def graph(request):
    return render(request, "graph.html")


def about(request):
    return render(request, "about.html")


def calculate_expression(request):  # мб на главную перенести ?
    """Веб-сервис, выполняющий вычисление выражения"""
    if request.method == 'POST':
        result: str = services.calculate_expression(request.POST.get('expression'))
        return render(request, "index.html", {'result': result})
    else:
        return HttpResponse(status=400)  # ???


def graph_expression(request):
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

# def calculate(request):
#     expression = request.GET.get('expression')
#     # Perform calculations on the expression string
#     result = evaluate_expression(expression)
#     # Return the result as JSON response
#     return JsonResponse({'result': result})


# def calculate_expression(request):
#     if request.method == 'POST':
#         expression = request.POST.get('expression')
#         double_num = request.POST.get('double_num')

#         # Perform calculations using the expression and double_num
#         # You can use eval() to evaluate the expression, but be cautious about potential security risks

#         # Evaluate the expression (example, but not recommended for production)
#         # result = eval(expression)
#         result = expression

#         # Pass the result back to the template for display
#         context = {'result': result}
#         return render(request, 'result.html', context)

#     # Handle GET request or other cases
#     return render(request, 'index.html')
