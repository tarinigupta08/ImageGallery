from django.shortcuts import render
from django.http import HttpResponse
from .models import task
# Create your views here.
def example_fun(request):
    task = task.objects.all()
    response = ""
    response= ",".join([task.title for task in tasks])
    return HttpResponse(response)
