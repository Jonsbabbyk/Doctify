
from django.contrib import admin
from django.urls import path, include
from doctor.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("doctor.urls")),
    path('', index, name='index'),
]
