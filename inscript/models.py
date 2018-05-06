from django.db import models
from enum import Enum
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Department(Enum):
    CS = "Computer Science"
    ESCOLAR = "Escolar"
    OTRO = "Otro Dpto."


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
    time_slot = models.TextField()
    lab_slot = models.TextField()
    responsability = models.IntegerField(default=100)
    in_english = models.BooleanField(default=False)
    is_honors = models.BooleanField(default=False)

    def __str__(self):
        return "{subject} - Gpo {group}".format(
            subject=self.subject, group=self.group_num
        )
