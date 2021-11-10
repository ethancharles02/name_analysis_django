from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

def todo(request):

    todo_items = range(1, 11)

    return render(request, 
        'todo/todo.html', 
        {"todo_items": todo_items}
        )