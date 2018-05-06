from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("courses_by/<str:teacher_id>", views.teacher_courses, name="teacher_courses"),
    path("courses_of/<str:subject>", views.subject_courses, "subject_courses"),
    path(
        "classrooms_at/<str:time_slot>",
        views.available_classrooms,
        "available_classrooms",
    ),
    path("teaching_at/<str:time_slot>", views.busy_teachers, "busy_teachers"),
    path(
        "not_teaching_at/<str:time_slot>",
        views.available_teachers,
        "available_teachers",
    ),
    path("course_at/<str:day>_<str:classroom>", views.which_course, "which_course"),
]
