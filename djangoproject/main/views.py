from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    context: dict={
        'title': 'LaSharm - Главная',
        # 'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context: dict = {
    }

    return render(request, 'main/about.html', context)

def delivery(request):
    context: dict = {
    }

    return render(request, 'main/dostavka.html', context)

