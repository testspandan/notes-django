from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_note/', views.add_note, name='add_note'),
]
