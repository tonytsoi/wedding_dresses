from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('dress/<str:pk>/', views.viewDress, name='dress'),
]