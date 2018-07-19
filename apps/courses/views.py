from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from .models import *

def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, "courses/index.html", context)

def create(request):
    course = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'], date=strftime("%Y-%m-%d %H:%M %p", gmtime()))
    return redirect('/')

def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'id': course.id,
        'name': course.name,
        'desc': course.desc
    }
    return render(request, "courses/delete.html", context)

def destroy(request, course_id):
    print(request.POST)
    if request.POST['yes']:
        Course.objects.get(id=course_id).delete()
    return redirect('/')