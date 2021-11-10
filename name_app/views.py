from django.shortcuts import render

def home(request):
    return render(
        request,
        'name_app/index.html',
        {
        }
    )