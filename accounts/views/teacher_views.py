from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate, login, logout
from ..serializers import UserSerializer, UserSignupSerializer, TeacherViewSerializer
from ..models.teacher import Teacher
from ..models.student import Student

class TeachersView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherViewSerializer
    
    