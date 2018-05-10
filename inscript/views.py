import json
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import Teacher, Classroom, Course, Subject

# Create your views here.


def index(request):
    return redirect(reverse("admin"))


def reportes(request):
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    courses = Course.objects.all()
    classrooms = Classroom.objects.all()
    context = {
        "teachers": teachers,
        "subjects": subjects,
        "courses": courses,
        "classrooms": classrooms,
    }
    return render(request, "inscript/reportes.html", context=context)


def teacher_courses(request, teacher_name):
    courses = Course.objects.filter(teacher__name=teacher_name)
    context = serializers.serialize("json", courses)
    return HttpResponse(json.dumps(context), content_type="application/json")


def subject_courses(request, subject_name):
    courses = Course.objects.filter(subject__name=subject_name)
    context = serializers.serialize("json", courses)
    return HttpResponse(json.dumps(context), content_type="application/json")


def available_classrooms(request, time_slot):
    classrooms = Classroom.objects.all()
    courses_given = Course.objects.filter(time_slot=time_slot)
    not_available = [course.classroom.number for course in courses_given]
    available = classrooms.exclude(number__in=not_available)
    context = serializers.serialize("json", available)
    return HttpResponse(json.dumps(context), content_type="application/json")


def busy_teachers(request, time_slot):
    courses = Course.objects.filter(time_slot=time_slot)
    busy_teachers = [course.teacher for course in courses]
    context = serializers.serialize("json", busy_teachers)
    return HttpResponse(json.dumps(context), content_type="application/json")


def available_teachers(request, time_slot):
    courses = Course.objects.filter(time_slot=time_slot)
    busy_teachers = [course.teacher.employee_id for course in courses]
    available = Teacher.objects.exclude(employee_id__in=busy_teachers)
    context = serializers.serialize("json", available)
    return HttpResponse(json.dumps(context), content_type="application/json")


def which_course(request, day, classroom):
    courses = Course.objects.filter(
        time_slot__contains=day, classroom__number=classroom
    )
    context = serializers.serialize("json", courses)
    return HttpResponse(json.dumps(context), content_type="application/json")


def validate_slot(request, classroom, time_slot):
    courses = Course.objects.filter(classroom=classroom, time_slot=time_slot)
    invalid = len(courses) > 0
    response = json.dumps({"invalid": invalid})
    return HttpResponse(response, content_type="application/json")
