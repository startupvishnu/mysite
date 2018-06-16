from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, Guys. We're building startup vishnu.")


def path1(request):
    return HttpResponse("This is path1 view")


def path2(request):
    return HttpResponse("This is path2 view")


def path3(request):
    context = {'name_of_organization': 'Vishnu Institute of Technology'}
    return render(request, "path3.html", context=context)
