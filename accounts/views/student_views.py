
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions


from ..serializers import StudentSerializer

from ..models.student import Student

#Index and create students
# /accounts/students GET
class StudentListView(generics.ListAPIView):
    """Index all teachers and create a new student The client API will make a POST call to this route automatically when a new student user is created"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
   
#Retrieve, update, delete a single teacher
# /accounts/students/<pk> GET, POST, PUT, PATCH, DELETE
class StudentRUDView(generics.RetrieveUpdateDestroyAPIView):
    """Detailed view, update, delete view for a single student"""
    permission_classes = [DjangoModelPermissions]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

