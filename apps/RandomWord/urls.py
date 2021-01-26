from django.urls import path
from . import views

app_name = 'random'
urlpatterns = [
	path('', views.index),
    path('reset', views.reset)
]