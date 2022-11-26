from django.db import models
from .course import Course
from accounts.models.student import Student
from ..utils import *

        

class Section(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="sections",
        blank=True
    )
    name = models.CharField(max_length=20)
    students = models.ManyToManyField(
        Student,
        related_name = "classes",
        blank=True,
    )
    
    
    
    #serializer will call to custom generation function when object is instantiated
    code = models.CharField(max_length=7, null=True)
    
    
    
    def __str__(self):
        return f"{self.course.name}: {self.name}"
    

        