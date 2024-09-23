from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('dress/<str:pk>/', views.viewDress, name='dress'),
    path('admin/', admin.site.urls),
]