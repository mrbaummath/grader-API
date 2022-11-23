from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import get_user_model, authenticate, login, logout
from ..serializers import UserSerializer, UserSignupSerializer
from ..models.teacher import Teacher
from ..models.student import Student


#custom user model
User = get_user_model()

# Create your views here.

# /accounts index
# GET /accounts/
class AccountsList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# /accounts/login/ user login 
#POST /accounts/login/

class LoginView(generics.CreateAPIView):
    
    serializer_class = UserSerializer
    
    def post(self, request):
        credentials = request.data
        user = authenticate(
            request, 
            username=credentials["username"],
            password=credentials["password"],
            )
        if user is not None:
            if user.is_active:
                login(request, user)

                if user.is_teacher:
                    request.session['account_type'] = 'teacher'
                    request.session['teacher_id'] = user.teacher.id
                elif user.is_student: 
                    request.session['account_type'] = 'student'
                    request.session['student_id'] = user.student.id
                return Response({
                    "user":{
                        "id": user.id,
                        "username": user.username,
                        "isTeacher": user.is_teacher,
                        "isStudent": user.is_student,
                    }
                })
            else:
                return Response(
                    {"msg": "Account is not active"}, 
                    status=status.HTTP_400_BAD_REQUEST,
                    )
        else:
            return Response(
                    {"msg": "Username and/or password is incorrect"}, 
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY
                    )
# /accounts logout 
class LogoutView(generics.DestroyAPIView):
    def delete(self,request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
