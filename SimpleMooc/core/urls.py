from django.urls import path

from SimpleMooc.core import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contac, name='contact'),
]
