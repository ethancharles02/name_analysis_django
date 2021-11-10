from django.urls import path
from ToDoApp.views import home
from ToDoApp.todo import todo
# from . import contact

urlpatterns = [
    # "" indicates the root url
    path("", home, name="home"),
    path("todo/todo.html", todo, name="todo")
]