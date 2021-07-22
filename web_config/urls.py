"""web_config URL Configuration

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
from django.contrib import admin
from django.urls import path
from home import views

from tjuhee import views as tjuheeviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.green_home),
    path('green_home',views.green_home),
    path('projects',views.projects),

    path('tjuhee/test',tjuheeviews.test),
    path('tjuhee/test01',tjuheeviews.test01),
    path('tjuhee/test03',tjuheeviews.test03),
]

