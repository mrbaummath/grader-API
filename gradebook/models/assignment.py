from django.db import models
from classes.models.course import Course
from accounts.models.teacher import Teacher

class Assignment(models.Model):
    
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='assignments'
    )
    
    grade_type_choices = [
        ('A', 'Letter Grade'),
        ('N', 'Numerical Grade')
    ]
    
    grade_type = models.CharField(
        max_length=1,
        choices=grade_type_choices
    )
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='assignments',
        related_query_name='assignment',
    )
    
    name = models.CharField(max_length=20)
    assigned_on = models.DateField()
    due_date = models.DateField()
    description = models.CharField(max_length=100)
    term= models.CharField(
        max_length=20,
        blank= True,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)