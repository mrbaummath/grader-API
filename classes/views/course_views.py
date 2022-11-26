from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from ..models.course import Course
from ..serializers import CourseListCreateSerializer, CourseRUDSerializer


# index and create route for courses 

class CoursesView(generics.ListCreateAPIView):
    serializer_class = CourseListCreateSerializer
    queryset = Course.objects.all()
    
 

class CourseRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRUDSerializer
        