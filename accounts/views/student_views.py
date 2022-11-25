
from rest_framework import generics

from ..serializers import StudentSerializer

from ..models.student import Student

#Index and create teachers
# /accounts/students GET, POST
class StudentListCreateView(generics.ListCreateAPIView):
    """Index all teachers and create a new student The client API will make a POST call to this route automatically when a new student user is created"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
   
#Retrieve, update, delete a single teacher
# /accounts/students/<pk> GET, POST, PUT, PATCH, DELETE
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Detailed view, update, delete view for a single student"""
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
