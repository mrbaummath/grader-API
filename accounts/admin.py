from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models.user import User
from .models.student import Student
from .models.teacher import Teacher

class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["id", "username", "email", "is_superuser", "is_student", "is_teacher"]
    
    fieldsets = (
      (None, {'fields': ('email', 'password', "is_student", "is_teacher")}),
      ('Permissions',
          {
              'fields': (
                  'is_active',
                  'is_staff',
                  'is_superuser',
              )
          }
      ),
      ('Dates', {'fields': ('last_login',)}),
    )
    # add_fieldsets is similar to fieldsets but it is used specifically
    # when you create a new user:
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_student', 'is_teacher')
        }),
    )




# Register user model w/ admin site
admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)


