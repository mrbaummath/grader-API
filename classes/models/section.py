from django.db import models
from .course import Course
from accounts.models.student import Student

class Section(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="sections"
    )
    name = models.CharField(max_length=20)
    students = models.ManyToManyField(
        Student,
        blank=True,
        null=True
    )