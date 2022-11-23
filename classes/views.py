from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from .models.section import Section
from .models.course import Course
from .serializers import CourseViewSerializer, CourseCUDSerializer
from accounts.models.user import User


# index and create route for courses 

class CoursesView(generics.ListCreateAPIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = CourseViewSerializer
    # GET /courses
    def get(self, request):
        """Index all courses GET /courses"""
        account_type = request.session["account_type"]
        
        if account_type == "teacher":
            teacher_id = request.session["teacher_id"]
            queryset = Course.objects.filter(teacher=teacher_id)
            serializer = CourseViewSerializer(queryset, many=True)
            print(request.user.id)
            return Response({
            'courses': serializer.data,
            'account_type': account_type
            })
        elif account_type == "student":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    def post(self, request):
        """Create Request POST /courses"""
        #copy request.data b/c request.data is immutable but the copy will be mutable
        course = request.data.copy()
        course["teacher"] = request.session["teacher_id"]
        course = CourseCUDSerializer(data=course)
        if course.is_valid():
            course.save()
            return Response({ 'course': course.data }, status=status.HTTP_201_CREATED)
        else:
            return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)


        
        