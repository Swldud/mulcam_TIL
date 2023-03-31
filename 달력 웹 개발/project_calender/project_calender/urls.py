
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('day/', include('day.urls')),
    path('month/', include('month.urls')),
]
