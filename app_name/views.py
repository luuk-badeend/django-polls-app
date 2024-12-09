from django.shortcuts import render


def index(request):
    return render(request, "app_name/index.html")

def second(request):
    return render(request, "app_name/second.html")