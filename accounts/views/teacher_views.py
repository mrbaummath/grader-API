from rest_framework import generics
from ..serializers import TeacherSerializer
from ..models.teacher import Teacher
from ..models.student import Student

#Index teachers. Note teacher creation is handled automatically when a user is created
# /accounts/teachers GET
class TeacherListCreateView(generics.ListCreateAPIView):
    """Index all teachers and create a new teacher. The client API will make a POST call to this route automatically when a new teacher user is created"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
   
#Retrieve, update, delete a single teacher
# /accounts/teachers/<pk> GET, POST, PUT, PATCH, DELETE
class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Detailed view, update, delete view for a single teacher"""
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

        
    

    
    