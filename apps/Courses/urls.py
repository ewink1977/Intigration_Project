from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.course_home, name = 'home'),
    path('add_course', views.add_course, name = 'add_course'),
    path('destroy/<killid>', views.destroy_course, name='destroy_course'),
    path('course/<courseid>', views.show_course, name='show_course'),
    path('add_comment/<courseid>', views.add_comment, name='add_comment'),
    path('user_courses/', views.add_user_to_course, name = 'student_add'),
    path('user_courses/add', views.process_add_user_to_course, name = 'process_student_add'),
]
