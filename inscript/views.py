import json
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Teacher, Classroom, Course

# Create your views here.


def index(request):
    return redirect("admin")


def teacher_courses(request, teacher_name):
    courses = Course.objects.filter(teacher__name=teacher_name)
    context = {"courses": courses}
    return HttpResponse(json.dumps(context), content_type='application/json')


def subject_courses(request, subject_name):
    courses = Course.objects.filter(subject__name=subject_name)
    context = {"courses": courses}
    return HttpResponse(json.dumps(context), content_type='application/json')


def available_classrooms(request, time_slot):
    classrooms = Classroom.objects.all()
    courses_given = Course.objects.filter(time_slot=time_slot)
    not_available = [course.classroom.number for course in courses_given]
    available = classrooms.exclude(number__in=not_available)
    context = {"classrooms": available}
    return HttpResponse(json.dumps(context), content_type='application/json')


def busy_teachers(request, time_slot):
    courses = Course.objects.filter(time_slot=time_slot)
    busy_teachers = [course.teacher for course in courses]
    context = {"teachers": busy_teachers}
    return HttpResponse(json.dumps(context), content_type='application/json')


def available_teachers(request, time_slot):
    courses = Course.objects.filter(time_slot=time_slot)
    busy_teachers = [course.teacher.employee_id for course in courses]
    available = Teacher.objects.exclude(employee_id__in=busy_teachers)
    context = {"teachers": available}
    return HttpResponse(json.dumps(context), content_type='application/json')


def which_course(request, day, classroom):
    courses = Course.objects.filter(
        time_slot__contains=day, classroom__number=classroom
    )
    context = {"courses": courses}
    return HttpResponse(json.dumps(context), content_type='application/json')
