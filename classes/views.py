from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from .models.section import Section
from .serializers import CourseSerializer
from accounts.models.user import User


# index and create route for courses 

class CoursesView(generics.ListCreateAPIView):
    
    serializer_class = CourseSerializer
    # GET /courses
    def get(self, request):
        """Index all courses"""
        user = User.objects.get(pk=request.user.id)
        if user.is_teacher:
            teacher = user.teacher
            queryset = teacher.courses.all()
            serializer = CourseSerializer(queryset, many=True)
            print(request.user.id)
            return Response({'courses': serializer.data})