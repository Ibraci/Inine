from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store', views.store, name='store'),
    path('connect', views.connect, name='connect'),
    path('show/<int:id>', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('destroy/<int:id>', views.destroy, name='destroy'),
    path('checked/<int:id>', views.checked, name='checked'),
]
