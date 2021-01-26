from django.urls import path
from . import views

app_name = 'random'
urlpatterns = [
	path('', views.index, name = 'home'),
    path('reset', views.reset, name = 'reset')
]