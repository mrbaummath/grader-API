from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import User
from .models.student import Student
from .models.teacher import Teacher

# Register user model w/ admin site
admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)


