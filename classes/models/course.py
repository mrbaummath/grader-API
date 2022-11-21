from django.db import models
from accounts.models.teacher import Teacher

class Course(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
