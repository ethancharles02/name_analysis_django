import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(
        request,
        'todo/index.html',
        {
        }
    )

def todo(request):
    return render(
        request,
        "todo/todo.html",
        {
        }
    )