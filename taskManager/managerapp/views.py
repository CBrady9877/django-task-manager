from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Worl!. You are at the managerapp index")

def detail(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)
   
def results(request, task_id):
    response = "You're looking at a list of task %s."
    return HttpResponse(response % task_id)

def complete(request, task_id):
    return HttpResponse("You're completing task %s." % task_id)