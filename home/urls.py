from django.urls import path
from. import views 
urlpatterns = [
    path('', views.home, name='home-home'),
    path('container', views.container, name='home-container')
]
