from django.db import models
from accounts.models.teacher import Teacher
from accounts.models.student import Student


class Course(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    
    terms = models.JSONField(default=dict)
    
    def students(self):
        student_ids = self.sections.values_list('students', flat=True)
        students = Student.objects.filter(id__in=student_ids)
        return students
    

    def __str__(self):
        return f"{self.name}"
