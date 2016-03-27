from django.shortcuts import render
from django.http import JsonResponse


def is_int(request, value):
    try:
        int(value)
        return JsonResponse({'response': True})
    except:
        return JsonResponse({'response': False})


def docs(request):
    return render(request, 'docs.html', {
        'question': True,
        'error_message': "no error.",
    })
