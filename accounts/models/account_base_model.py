from django.conf import settings
from django.db import models

#Generic Account abstract base class

class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user"
    )
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True