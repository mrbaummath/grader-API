from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register user model w/ admin site
admin.site.register(User, UserAdmin)

