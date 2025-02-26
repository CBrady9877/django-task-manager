from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def user_view(request):
    return HttpResponse("User page")