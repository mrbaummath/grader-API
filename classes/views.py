from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from .models.course import Course
from .models.section import Section
from .serializers import CourseSerializer
from accounts.models.teacher import Teacher
from accounts.models.student import Student
from accounts.models.user import User


# index and create route for courses 

class CoursesView(generics.ListCreateAPIView):
    
    serializer_class = CourseSerializer
    # GET /courses
    def get(self, request):
        """Index all courses"""
        user = User.objects.get(pk=request.user.id)
        if user.isTeacher:
            teacher = Teacher.objects.get(user=user.id)
            queryset = teacher.courses.all()
            serializer = CourseSerializer(queryset, many=True)
            print(request.user.id)
            return Response({'courses': serializer.data})