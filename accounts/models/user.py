from django.db import models
#import Django's built in User model
from django.contrib.auth.models import AbstractUser

#custom User model will track whether user is a teacher or student. Within the gradebook app, a teacher or student account will reference the user by foreign key in a one-to-one relationship

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

