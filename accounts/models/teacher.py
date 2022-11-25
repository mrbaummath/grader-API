from django.db import models
from .account_base_model import Account



#Teacher specific account model
class Teacher(Account):
    title = models.CharField(
        max_length = 20,
        blank=True
    )
    
      
    def __str__(self):
        honorific = self.title if len(self.title) > 0 else "Instructor"
        return f"{honorific} {self.last_name}"
    
    def create(self, **validated_data):
        print(f"**THIS IS DATA********** {validated_data}")
        teacher = self.model(validated_data)
        teacher.save()
        return teacher
    
    

    