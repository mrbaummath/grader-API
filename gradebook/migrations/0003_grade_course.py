# Generated by Django 4.1.3 on 2022-11-29 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_course_student_grades'),
        ('gradebook', '0002_alter_grade_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='classes.course'),
            preserve_default=False,
        ),
    ]
