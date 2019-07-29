from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from SimpleMooc.core import views
app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contac, name='contact'),
]