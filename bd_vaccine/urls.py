"""bd_vaccine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from vaccine import views

from .views import *
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin/', auth_view.LoginView.as_view(template_name='registration/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard/',admin_dashboard_view,name = 'admin-dashboard'),
    path('',index,name='index'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('vaccine-list/',views.vaccine_list,name='vaccine_list'),
    path('vaccine/', include('vaccine.urls', namespace='vaccine')),
    path('patient/',include('profiles.urls',namespace='patient')),
    #path('admin-dashboard',admin_dashboard_view,name='admin-dashboard')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)