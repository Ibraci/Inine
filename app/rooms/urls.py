from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:id>/', views.show, name='show'),
    path('store', views.store, name='store'),
    path('destroy/<int:id>/', views.destroy, name='destroy'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
]
