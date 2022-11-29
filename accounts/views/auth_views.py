from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
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

class LoginView(APIView):
    permission_classes=[]
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
                    return Response({
                        "user":{
                            "id": user.id,
                            "teacherId": user.teacher.id,
                            "username": user.username,
                            "token": user.get_auth_token(),
                            "type": 'teacher',
                            "firstName": user.teacher.first_name,
                            "lastName": user.teacher.last_name,
                            "email": user.teacher.email,
                            "pronouns": user.teacher.pronouns,
                            "title": user.teacher.__str__(),
                        }
                    })
                elif user.is_student:
                    return Response({
                        "user":{
                            "id": user.id,
                            "studentId": user.student.id,
                            "username": user.username,
                            "token": user.get_auth_token(),
                            "type": 'student',
                            "firstName": user.student.first_name,
                            "lastName": user.student.last_name,
                            "email": user.student.email,
                            "pronouns": user.student.pronouns,
                            "name": user.student.__str__(),
                            "year": user.student.year,
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
        request.user.delete_token()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

#
class UserSignupView(generics.CreateAPIView):
    authorization_classes = ()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSignupSerializer
    
    # def post(sel, request):
    #     print(f"************sdfkljdfkjdfjkldjklf***********{request.data}")
    #     return Response(status=status.HTTP_204_NO_CONTENT)
