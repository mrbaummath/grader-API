from rest_framework.permissions import DjangoModelPermissions
from rest_framework import generics, status
from ..models.assignment import Assignment
from ..serializers import AssignmentSerializer
from rest_framework.response import Response
from accounts.models.student import Student
from classes.models.section import Section

class AssignmentListCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = AssignmentSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Assignment.objects.all()
        elif user.is_teacher:
            return Assignment.objects.filter(teacher=user.teacher)
        else:
            return None

#teacher view to see, update, delete assignments 
class AssignmentRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = AssignmentSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Assignment.objects.all()
        elif user.is_teacher:
            return Assignment.objects.filter(teacher=user.teacher)
        else:
            return None

#view for a student to see their assignments.
class StudentAssignmentView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = AssignmentSerializer
    
    def get_queryset(self):
        user = self.request.user
        #only accessible to the logged in student
        if user.is_student:
            #generat the queryset which includes all courses the student belongs to
            student_courses = Student.objects.get(pk=user.student.id).classes.values_list('course', flat=True)
            #grab any assignments associated with those courses
            assignments = Assignment.objects.filter(course_id__in = student_courses)
            return assignments
        else:
            return None