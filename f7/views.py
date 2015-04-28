from django.shortcuts import render


def index(request):
    return render(request, 'f7/index.html')