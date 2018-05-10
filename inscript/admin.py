from django.contrib import admin
from .models import Teacher, Classroom, Course, Subject


class MyAdmin(admin.AdminSite):
    site_title = "Admin Site"
    site_header = "Inscribetec"
    index_title = "Administración de Inscribetec"


class CourseAdmin(admin.ModelAdmin):
    class Media:
        js = ("inscript/course_validation.js",)


# Register your models here.
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject)
