# Generated by Django 4.1.3 on 2022-11-29 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_student_email_teacher_email'),
        ('gradebook', '0002_alter_grade_feedback'),
        ('classes', '0005_course_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='student_grades',
            field=models.ManyToManyField(through='gradebook.Grade', to='accounts.student'),
        ),
    ]
