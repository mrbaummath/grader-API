
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import generics
from ..models.section import Section
from ..serializers import SectionListCreateSerializer, SectionRUDSerializer, StudentSectionListSerializer
from accounts.models.student import Student
from django.shortcuts import get_object_or_404
from ..models import Course


# index and create route for sections from a specific course. Section creation can also be done while creating a course. Students will not have access to this view and will access their sections differently

# /courses/<course_id>/sections GET POST
#For the POST request, client only needs to provide a name keyword
class SectionListCreateView(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = SectionListCreateSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_teacher or user.is_superuser:
            course_id = self.kwargs["course_id"]
            course = get_object_or_404(Course, pk=course_id)
            if course.teacher == user.teacher or user.is_superuser:
                return Section.objects.filter(course=course_id)
        else:
            return []
        
#detail, update, delete view for a section
# /courses/<course_id>/sections/<section_id> GET PUT PATCH DELETE
class SectionRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = SectionRUDSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_teacher or user.is_superuser:
            course_id = self.kwargs["course_id"]
            pk = self.kwargs["pk"]
            course = get_object_or_404(Course, pk=course_id)
            if course.teacher == user.teacher or user.is_superuser:
                return Section.objects.filter(id=pk)
        else:
            return []
    

#view for a student to retrieve class information. Uses request context so it is not accessible to anyone who is not logged in as the student

# /courses/myclasses GET
class StudentSectionList(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = StudentSectionListSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_student:
            student = Student.objects.get(user=user.id)
            return student.classes.all()
        else:
            return []
        