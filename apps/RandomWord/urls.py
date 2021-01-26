from django.urls import path
from . import views

app_name = 'random'
urlpatterns = [
	path('', views.random_index, name = 'home'),
    path('reset', views.rand_reset, name = 'reset')
]