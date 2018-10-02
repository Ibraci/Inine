from django.urls import path

from . import views

urlpatterns = [
    path('103', views.error103),
]
