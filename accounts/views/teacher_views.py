from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from ..serializers import TeacherSerializer
from ..models.teacher import Teacher
from ..models.student import Student

#Index and create teachers
# /accounts/teachers GET, POST
class TeacherListCreateView(generics.ListCreateAPIView):
    """Index all teachers and create a new teacher. The client API will make a POST call to this route automatically when a new teacher user is created"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
class TeacherDetailView(APIView):
    serializer_class = TeacherSerializer
    def get(self, request, pk):
        return Response(data=request.session)
        
    

    
    