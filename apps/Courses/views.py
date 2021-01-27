from .models import CourseComments, Courses, Descriptions
from django.shortcuts import render, redirect
from django.contrib import messages
from ..LoginAndRegistration.models import User

def course_home(request):
    context = {
        "courses" : Courses.objects.all(),
        "descriptions" : Descriptions.objects.all(),
    }
    return render(request, 'html/home.html', context)

def add_course(request):
    if request.method == 'POST':
        errors = Courses.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='danger')
            return redirect('home')
        else:
            newcourse = Courses.objects.create(name=request.POST['coursename'])
            Descriptions.objects.create(desc=request.POST['coursedesc'], course=newcourse)
            messages.success(request, f"{ request.POST['coursename'] } has been created successfully!")
            return redirect('course:home')

def destroy_course(request, killid):
    if request.method == 'GET':
        context = {
            'killinfo' : Courses.objects.get(id=killid)
        }
        return render(request, 'html/destroy.html', context)
    if request.method == 'POST':
        byebye = Courses.objects.get(id=killid)
        byebye.delete()
        return redirect('course:home')

def show_course(request, courseid):
    context = {
        "courseinfo" : Courses.objects.get(id=courseid),
        "comments" : CourseComments.objects.filter(course_comment=courseid),
    }
    return render(request, 'html/coursepage.html', context)

def add_comment(request, courseid):
    if request.method == 'POST':
        attachto = Courses.objects.get(id=courseid)
        CourseComments.objects.create(user=request.POST['commentor'], text=request.POST['commentbody'], course_comment=attachto)
        messages.success(request, f"Comment successfully added.")
    return redirect('course:show_course', courseid)

def add_user_to_course(request):
    context = {
        'courses': Courses.objects.all(),
        'users': User.objects.all(),
    }
    return render(request, 'html/adduser.html', context)

def process_add_user_to_course(request):
    if request.method == 'POST':
        student = User.objects.get(id = request.POST['userid'])
        course = Courses.objects.get(id = request.POST['courseid'])
        course.student.add(student)
        messages.success(request, f"{student.first_name} has been added to {course.name}.")
        return redirect('course:student_add')
    else:
        return redirect('course:home')