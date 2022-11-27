from django.db import models
from .assignment import Assignment
from accounts.models.student import Student

class Grade(models.Model):
    
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name='grades'
    )
    
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='grades'
    ) 
    
    feedback = models.TextField()
    
    value = models.CharField(max_length=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
        
    

    
    