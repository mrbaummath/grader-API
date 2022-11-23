from django.db import models
#import Django's built in User model
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from .student import Student

#custom User model will track whether user is a teacher or student. Within the gradebook app, a teacher or student account will reference the user by foreign key in a one-to-one relationship

class UserManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,**validated_data):
        """Create a new user profile"""
        print("*********I AM BEING USED********")
        # take out data which won't be passed to directly creating user
        teacher_code = validated_data.pop("teacher_code", None)
        year_in_school = validated_data.pop("year_in_school", None)
        password = validated_data.pop("password")
        #remove these from the data
        user = self.model(**validated_data)
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()


        
    

