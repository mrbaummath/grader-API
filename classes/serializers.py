from rest_framework import serializers
from .models.course import Course
from .models.section import Section

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'