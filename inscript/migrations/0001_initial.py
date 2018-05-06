# Generated by Django 2.0.4 on 2018-05-02 22:07

from django.db import migrations, models
import django.db.models.deletion
import inscript.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('capacity', models.IntegerField(default=1)),
                ('administrator', models.CharField(choices=[(inscript.models.Department('Computer Science'), 'Computer Science'), (inscript.models.Department('Escolar'), 'Escolar'), (inscript.models.Department('Otro Dpto.'), 'Otro Dpto.')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_num', models.IntegerField(default=1)),
                ('time_slot', models.TextField()),
                ('lab_slot', models.TextField()),
                ('responsability', models.IntegerField(default=100)),
                ('in_english', models.BooleanField(default=False)),
                ('is_honors', models.BooleanField(default=False)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inscript.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=8, unique=True)),
                ('name', models.CharField(max_length=25)),
                ('lab_hours', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=9, unique=True)),
                ('name', models.CharField(max_length=25)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('num_classes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inscript.Subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(to='inscript.Teacher'),
        ),
    ]