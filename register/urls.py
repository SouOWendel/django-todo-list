from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
		path('success', views.success, name='success'),
		path('reset_pass', views.reset_pass, name='reset_pass'),
		path('reset_success', views.reset_success, name='reset_success'),
]