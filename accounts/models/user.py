from django.db import models
#import Django's built in User model
from django.contrib.auth.models import AbstractUser

#custom User model will track whether user is a teacher or student. Within the gradebook app, a teacher or student account will reference the user by foreign key in a one-to-one relationship

class User(AbstractUser):
    isTeacher = models.BooleanField(default=False)
    isStudent = models.BooleanField(default=False)
    

