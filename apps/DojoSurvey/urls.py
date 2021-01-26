from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [
	path('', views.survey_home, name = 'home'),
    path('result', views.result, name = 'result'),
    path('redir', views.redir, name = 'redir'),
]