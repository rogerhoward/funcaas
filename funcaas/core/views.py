from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

def home(request):
    return render(request, 'home.html', {
        'modules': settings.CUSTOM_APPS,
    })
