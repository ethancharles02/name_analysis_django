from django.urls import path
from name_app.views import home
from name_app.names import name_form

urlpatterns = [
    # "" indicates the root url
    path("", home, name="home"),
    path("name_app/name_request.html", name_form, name="name_request"),
    path("name_data", name_form, name="name_data"),
]