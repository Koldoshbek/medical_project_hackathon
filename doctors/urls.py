"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from doctors import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/<int:index_id>/deny', views.deny, name='deny'),
    path('get/<int:index_id>/accept', views.accept, name='accept'),
    path('get/<int:index_id>/delete', views.delete_app, name='delete'),
    path('get/<int:index_id>/doctors', views.getDoctors, name='getDoctors'),
    path('get/<int:index_id>/Info', views.getInfo, name='getInfo'),
    path('get/<int:index_id>/page', views.doctorsPage, name='doctorsPage'),
    path('get/<int:index_id>/app', views.appointments, name='appointments'),
    path('get/<int:index_id>time/', views.time, name='time'),

]
