# Generated by Django 4.1.3 on 2022-12-01 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_course_student_grades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='student_grades',
        ),
    ]