
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions



from ..serializers import StudentSerializer

from ..models.student import Student

#Note that on sign-up, a Student object is created via the User serializer create function if the user is a student

#There is a student create view here, but it's intended purpose is to be used to instantiate a student w/o a user associated with it only when a teacher adds a student to one of their sections but that student has not signed up for their own account

#Index all students who have a user account associated with them --> needed to help a teacher add a student to a section when that student already has an account
# /accounts/students GET 

class StudentListCreateView(generics.ListCreateAPIView):
    """Index all teachers and create a new student The client API will make a POST call to this route automatically when a new student user is created"""
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
 

    
   
#Retrieve, update, delete a single teacher
# /accounts/students/<pk> GET, POST, PUT, PATCH, DELETE
class StudentRUDView(generics.RetrieveUpdateDestroyAPIView):
    """Detailed view, update, delete view for a single student"""
    permission_classes = [DjangoModelPermissions]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    



