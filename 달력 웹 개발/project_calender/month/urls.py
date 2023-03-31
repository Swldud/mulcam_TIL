from django.urls import path

from . import views

urlpatterns = [
    path('month_main/', views.month_main),
]