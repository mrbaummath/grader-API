from django.contrib import admin
from .models.course import Course
from .models.section import Section

# Register your models here.
admin.site.register(Course)
admin.site.register(Section)