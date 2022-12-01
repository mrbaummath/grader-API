from django.db import models


class Grade(models.Model):
    
    assignment = models.ForeignKey(
        "Assignment",
        on_delete=models.CASCADE,
        related_name='grades'
    )
    
    student = models.ForeignKey(
        "accounts.Student",
        on_delete=models.CASCADE,
        related_name='grades'
    ) 
    
    course = models.ForeignKey(
        "classes.Course",
        on_delete = models.CASCADE,
        related_name = 'grades'
    )
    
    feedback = models.TextField()
    
    value = models.CharField(max_length=10)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
        
    

    
    