from django.db import models
#import Django's built in User model
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager

#custom User model will track whether user is a teacher or student. Within the gradebook app, a teacher or student account will reference the user by foreign key in a one-to-one relationship

class UserManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, username, email, password=None, is_student=False, is_teacher=False, **extra_fields):
        """Create a new user profile"""
        user = self.model(username=username,email=self.normalize_email(email), is_teacher=is_teacher, is_student=is_student, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


        
    

