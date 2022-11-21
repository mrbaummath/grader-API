from django.db import models
from .account_base_model import Account

#Teacher specific account model
class Student(Account):
    
    YEAR_CHOICES = [
    ("FR", "First Year"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
]
    
    year = models.CharField(
        max_length = 2,
        choices = YEAR_CHOICES,
    )
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
