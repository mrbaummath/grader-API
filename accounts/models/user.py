from django.db import models
#import Django's built in User model
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager



#custom User model will track whether user is a teacher or student. Within the gradebook app, a teacher or student account will reference the user by foreign key in a one-to-one relationship

class UserManager(BaseUserManager):
    """Manager for user profiles (user model and account)"""
    
    #function to create a teacher
    # def create_teacher(**teacher_fields):
    #     pass
        
        
    def create_user(self,**validated_data):
        """Create a new user profile and associated account type"""
        #take out password to set later
        password = validated_data.pop("password")
        #set password
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


        
    

