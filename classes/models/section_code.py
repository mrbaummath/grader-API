from django.db import models
from .section import Section

class SectionCode(models.Model):
    code = models.CharField(max_length=10)
    
    section = models.OneToOneField(
        Section,
        on_delete = models.CASCADE,
        related_name = "code"
    )