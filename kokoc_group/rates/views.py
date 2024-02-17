from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Rate


def index(request):
    date = request.GET.get('date')
    charcode = request.GET.get('charcode')
    rate = get_object_or_404(Rate, date=date, charcode=charcode)
    data = {
        'date': date,
        'charcode': charcode,
        'rate': rate.rate
    }
    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
