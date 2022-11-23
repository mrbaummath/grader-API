from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from ..models.course import Course
from ..serializers import CourseViewSerializer, CourseCUDSerializer


# index and create route for courses 

class CoursesView(generics.ListCreateAPIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [DjangoModelPermissions]
    serializer_class = CourseViewSerializer
    
    def get_queryset(self):
        if self.request.session["account_type"]:
            account_type = self.request.session["account_type"]
            if account_type == "teacher":
                teacher_id = self.request.session["teacher_id"]
                return Course.objects.filter(teacher=teacher_id)
            else:
                return None
        else:
            return None
    
    
   
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

class CourseRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseViewSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        """View single course details GET /courses/course_id"""
        self.serializer_class = CourseCUDSerializer
        account_type = request.session["account_type"]
        if account_type == "teacher":
            course = get_object_or_404(Course, pk=pk)
            course_serializer = CourseViewSerializer(course)
            return Response({'course': course_serializer.data})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, pk):
        account_type = request.session["account_type"]
        if account_type == 'teacher':
            course = get_object_or_404(Course, pk=pk)
            if request.session["teacher_id"] == course.teacher.id:
                course.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                raise PermissionDenied('Unauthorized, this is not your course')
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    def partial_update(self, request, pk):
        self.serializer_class = CourseCUDSerializer
        account_type = request.session["account_type"]
        if account_type == 'teacher':
            course = get_object_or_404(Course, pk=pk)
            course_update = CourseCUDSerializer(course, data=request.data, partial=True)
            if request.session["teacher_id"] == course.teacher.id:
                if course_update.is_valid():
                    course_update.save()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response(course_update.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise PermissionDenied('Unauthorized, this is not your course')
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        