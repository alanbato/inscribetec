import json
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import Teacher, Classroom, Course, Subject, TimeSlot, Department

# Create your views here.


def index(request):
    return redirect("http://inscribetec.herokuapp.com/admin")


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
    courses = Course.objects.filter(teacher__employee_id=teacher_name)
    cont = []
    for course in courses:
        cont.append(
            {
                "clave": course.subject.key,
                "grupo": course.group_num,
                "horario": TimeSlot[course.time_slot].value,
                "salon": course.classroom.number,
                "idioma": course.in_english,
                "honors": course.is_honors,
            }
        )
    # context = serializers.serialize("json", courses)
    context = json.dumps(cont)
    return HttpResponse(context, content_type="application/json")


def subject_courses(request, subject_name):
    courses = Course.objects.filter(subject__key=subject_name)
    cont = []
    for course in courses:
        cont.append(
            {
                "clave": course.subject.key,
                "grupo": course.group_num,
                "profesor": ", ".join(teacher.name for teacher in course.teacher.all()),
                "horario": TimeSlot[course.time_slot].value,
                "salon": course.classroom.number,
                "idioma": course.in_english,
                "honors": course.is_honors,
            }
        )
    # context = serializers.serialize("json", courses)
    context = json.dumps(cont)
    return HttpResponse(context, content_type="application/json")


def available_classrooms(request, time_slot):
    classrooms = Classroom.objects.all()
    courses_given = Course.objects.filter(time_slot=time_slot)
    not_available = [course.classroom.number for course in courses_given]
    available = classrooms.exclude(number__in=not_available)
    cont = []
    for room in available:
        cont.append(
            {
                "salon": room.number,
                "cap": room.capacity,
                "admin": Department[room.administrator].value,
            }
        )

    # context = serializers.serialize("json", available)
    return HttpResponse(json.dumps(cont), content_type="application/json")


def busy_teachers(request, time_slot):
    courses = Course.objects.filter(time_slot=time_slot)
    busy_teachers = [teacher for course in courses for teacher in course.teacher.all()]
    cont = []
    for teacher in busy_teachers:
        cont.append(
            {
                "id": teacher.employee_id,
                "name": teacher.name,
                "phone": teacher.telephone,
                "email": teacher.email,
                "groups": teacher.num_classes,
            }
        )
    # context = serializers.serialize("json", busy_teachers)
    return HttpResponse(json.dumps(cont), content_type="application/json")


def available_teachers(request, time_slot):
    courses = Course.objects.filter(time_slot=time_slot)
    busy_teachers = [teacher.id for course in courses for teacher in course.teacher]
    available = Teacher.objects.exclude(employee_id__in=busy_teachers)
    cont = []
    for teacher in available:
        cont.append(
            {
                "id": teacher.employee_id,
                "name": teacher.name,
                "phone": teacher.telephone,
                "email": teacher.email,
                "groups": teacher.num_classes,
            }
        )
    return HttpResponse(json.dumps(cont), content_type="application/json")


def which_course(request, day, classroom):
    courses = Course.objects.filter(
        time_slot__contains=day.upper(), classroom__number=classroom
    )
    cont = []
    for course in courses:
        cont.append(
            {
                "clave": course.subject.key,
                "grupo": course.group_num,
                "profesor": ", ".join(teacher.name for teacher in course.teacher.all()),
                "horario": TimeSlot[course.time_slot].value,
                "idioma": course.in_english,
                "honors": course.is_honors,
            }
        )
    return HttpResponse(json.dumps(cont), content_type="application/json")


def validate_slot(request, classroom, time_slot):
    courses = Course.objects.filter(classroom=classroom, time_slot=time_slot)
    invalid = len(courses) > 0
    response = json.dumps({"invalid": invalid})
    return HttpResponse(response, content_type="application/json")
