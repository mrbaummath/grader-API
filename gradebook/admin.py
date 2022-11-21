from django.contrib import admin
from .models.assignment import Assignment
from .models.grade import Grade

# Register your models here.
admin.site.register(Assignment)
admin.site.register(Grade)