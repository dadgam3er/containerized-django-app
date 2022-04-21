from ssl import HAS_TLSv1_3
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("Hello Sami")