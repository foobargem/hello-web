from django.shortcuts import render
from django.http import HttpResponse


def healthcheck(request):
    return HttpResponse('', status=200)
