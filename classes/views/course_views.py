
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import generics
from ..models.course import Course
from ..serializers import CourseListCreateSerializer, CourseRUDSerializer
from accounts.models.user import User
from django.shortcuts import get_object_or_404


# index and create route for courses. This view can also be used to create related sections (see the serializer, which includes nested writale views of the sections)
# /courses GET, POST
class CourseListCreateView(generics.ListCreateAPIView):
    """Index and create courses. Can also be used to create sections for a course while creating it"""

    serializer_class = CourseListCreateSerializer
    #restrict queryet to current teacher user (or return all if superuser). Students do not have access to course level views
    def get_queryset(self):
        user = self.request.user
        if user.is_teacher:
            return Course.objects.filter(teacher=user.teacher)
        elif user.is_superuser:
            return Course.objects.all()
        else:
            return []
        
    
#detail, update and delete route for courses. This will primarily also be used for teachers to view sections on the client side (though in theory the section views here would serve just fine)
# /courses/<course_id> GET, PUT, PATCH, DELETE
class CourseRUDView(generics.RetrieveUpdateDestroyAPIView):
    """Detail view, updating, and deleting sections"""

    serializer_class = CourseRUDSerializer
    #restrict queryet to current teacher user (or return all if superuser). Students do not have access to course level views
    def get_queryset(self):
        user = self.request.user
        if user.is_teacher:
            return Course.objects.filter(teacher=user.teacher)
        elif user.is_superuser:
            return Course.objects.all()
        else:
            return []


        
        