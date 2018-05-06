from django.contrib import admin

from .models import Teacher, Classroom, Course, Subject

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(Subject)
