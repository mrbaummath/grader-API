from rest_framework.permissions import DjangoModelPermissions
from rest_framework import generics, status
from ..models.assignment import Assignment
from ..serializers import AssignmentSerializer, GradeSerializer
from rest_framework.response import Response
from accounts.models.student import Student
from classes.models.section import Section
from ..models.grade import Grade

#list / create grades for a given assignment
# if creating, client will provide all information 
# /gradebook/<assignment_id>/grades/
class AssignmentGradesListCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = GradeSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_teacher:
            assignment_id = self.kwargs["assignment_id"]
            return Grade.objects.filter(assignment=assignment_id)

#view for teacher to update, read, destroy a grade which they assigned. Can also be used by a student for GET only
# /gradebook/grades/<grade_id>
class GradeRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = GradeSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Grade.objects.all()
        elif user.is_teacher:
            return Grade.objects.filter(assignment__teacher = user.teacher.id)
        elif user.is_student and self.request.method == "POST":
            return Grade.objects.filter(student=user.student.id)
        else:
            return None

#view for student to see all of their grades
#/gradebook/mygrades/
class StudentGradesView(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = GradeSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_student:
            return Grade.objects.filter(student = user.student.id)
        else:
            return None
    