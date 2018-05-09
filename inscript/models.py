from django.db import models
from enum import Enum
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Department(Enum):
    CS = "Computer Science"
    ESCOLAR = "Escolar"
    OTRO = "Otro Dpto."


class TimeSlot(Enum):
    MAVI7 = "MaVi 7/3"
    MAVI8 = "MaVi 8+/3"
    MAVI10 = "MaVi 10/3"
    MAVI11 = "MaVi 11+/3"
    MAVI13 = "MaVi 13/3"
    MAVI14 = "MaVi 14+/3"
    MAVI16 = "MaVi 16/3"
    MAVI18 = "MaVi 18/3"
    MAVI19 = "MaVi 19+/3"
    LUJU7 = "LuJu 7/3"
    LUJU8 = "LuJu 8+/3"
    LUJU10 = "LuJu 10/3"
    LUJU11 = "LuJu 11+/3"
    LUJU13 = "LuJu 13/3"
    LUJU14 = "LuJu 14+/3"
    LUJU16 = "LuJu 16/3"
    LUJU18 = "LuJu 18/3"
    LUJU19 = "LuJu 19+/3"
    MI7 = "Mi 7/6"
    MI10 = "Mi 10/6"
    MI13 = "Mi 13/6"
    MI14 = "Mi 14+/6"


class Teacher(models.Model):
    employee_id = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=25)
    telephone = PhoneNumberField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

    @property
    def num_classes(self):
        return len(Course.objects.filter(teacher__employee_id=self.employee_id))


class Classroom(models.Model):
    number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField(default=1)
    administrator = models.CharField(
        max_length=10, choices=[(tag.name, tag.value) for tag in Department]
    )

    def __str__(self):
        return self.number


class Subject(models.Model):
    key = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=25)
    lab_hours = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    classroom = models.ForeignKey(Classroom, on_delete=models.PROTECT)
    teacher = models.ManyToManyField(Teacher)
    group_num = models.IntegerField(default=1)
    time_slot = models.CharField(
        max_length=10, choices=[(tag.name, tag.value) for tag in TimeSlot]
    )
    lab_slot = models.CharField(
        max_length=10, choices=[(tag.name, tag.value) for tag in TimeSlot]
    )
    responsability = models.IntegerField(default=100)
    in_english = models.BooleanField(default=False)
    is_honors = models.BooleanField(default=False)

    def __str__(self):
        return "{subject} - Gpo {group}".format(
            subject=self.subject, group=self.group_num
        )
