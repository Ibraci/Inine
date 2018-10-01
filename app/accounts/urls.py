from django.urls import path

from . import views

urlpatterns = [
    path('profile', views.profile),
    path('update', views.update),
    path('password', views.password),
    path('login', views.index),
    path('store', views.store),
    path('logout', views.logout_view)
]
