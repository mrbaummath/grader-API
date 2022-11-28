from django.db import models
#import Django's built in User model
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from rest_framework.authtoken.models import Token


#custom User model will track whether user is a teacher or student. Within the gradebook app, a teacher or student account will reference the user by foreign key in a one-to-one relationship

class UserManager(BaseUserManager):
    """Manager for user profiles (user model and account)"""
    
    #function to create a teacher
    # def create_teacher(**teacher_fields):
    #     pass
        
        
    def create_user(self, **validated_data):
        """Create a new user profile and associated account type"""
        #take out password to set later
        password = validated_data.pop("password")
        #set password
        user = self.model(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,**data):
        """Create and save a new superuser with given details"""


        user = self.create_user(**data)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
    
    
    

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    def get_auth_token(self):
        Token.objects.filter(user=self).delete()
        token = Token.objects.create(user=self)
        self.token = token.key
        self.save()
        return token.key

    def delete_token(self):
        Token.objects.filter(user=self).delete()
        self.token = None
        self.save()
        return self


        
    

