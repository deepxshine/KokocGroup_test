from django.http import JsonResponse


def tr_handler404(request, exception):

    return JsonResponse(data={
        'status': '404 Not Found',
        'detail': 'Данные по вашему запросу не найдены'
    }, json_dumps_params={'ensure_ascii': False})


def tr_handler500(request):
    """
    Обработка ошибки 500
    """
    return JsonResponse(data={
        'status': '500 Internal Server Error',
        'detail': ('Ошибка обработки запроса.'
                   'Проверьте правильность введенных данных')
    }, json_dumps_params={'ensure_ascii': False})
