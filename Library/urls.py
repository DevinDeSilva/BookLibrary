from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage),
    path('add', views.addBook),
    path('delete', views.deleteBook),
]
