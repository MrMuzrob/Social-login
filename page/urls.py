from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstPage, name='first_page')
]