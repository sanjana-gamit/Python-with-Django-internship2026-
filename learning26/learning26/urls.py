# learning26/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 👇 THIS MUST EXIST
    path('', views.home, name='home'),

    path('services/', include('services.urls')),
    path('student/', include('student.urls')),
    path('employee/', include('employee.urls')),
]