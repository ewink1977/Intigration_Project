from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [
	path('', views.index),
    path('result', views.result),
    path('redir', views.redir),
]