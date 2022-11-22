from django.contrib import admin
from .models.user import User
from .models.student import Student
from .models.teacher import Teacher


#inline for custom user model
class UserInline(admin.StackedInline):
    model = User
    can_delete=False
    verbose_name_plural='user'
    



# Register user model w/ admin site
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)


