from .models.assignment import Assignment
from accounts.models import Student

student_courses = Student.obejcts.all().values_list('classes')

print(student_courses)