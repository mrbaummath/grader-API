from rest_framework import serializers
from .models.course import Course
from .models.section import Section

#serializer for viewing a course
class CourseViewSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()
    class Meta:
        model = Course
        fields = ('teacher','name', 'subject')

#serializer for creating, updating, destroying a course
class CourseCUDSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Course
        fields = ("name", "subject","teacher")