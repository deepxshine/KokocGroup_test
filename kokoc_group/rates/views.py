from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Rate


def index(request):
    date = request.GET.get('date')
    charcode = request.GET.get('charcode')
    rate = Rate.objects.filter(date=date, charcode=charcode).first()
    if rate:
        data = {
            'date': date,
            'charcode': charcode,
            'rate': rate.rate
        }
        return JsonResponse(data=data, json_dumps_params={'ensure_ascii': 
                                                          False})
    return JsonResponse(data={
        'status': '404 Not Found',
        'detail': ('Данные по вашему запросу не найлены')
    }, json_dumps_params={'ensure_ascii': False})
