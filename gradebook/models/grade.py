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
    
    feedback = models.CharField(max_lenth='300')
    
    def set_grade_type(self):
        if self.assignment.grade_type == 'A':
            return models.CharField(max_length='10')
        elif self.assignment.grade_type == 'N':
            return models.DecimalField(
                max_digits=3, 
                decimal_places=2,
            )
    
    value = set_grade_type()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
        
    

    
    