from django.conf import settings
from django.db import models

#Generic Account abstract base class

class Account(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s",
        blank=True,
        null=True
        
    )
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=100)
    email = models.CharField(
        max_length = 100, 
        null=False,
        unique=True
        )
    
    
    class Meta:
        abstract = True