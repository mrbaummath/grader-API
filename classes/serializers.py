from rest_framework import serializers
from .models.course import Course
from .models.section import Section
from accounts.serializers import StudentSerializer
from accounts.models import Student
from .utils import *

#section serializer for nested representation w/in a course. This willbe used w/in the Course create/update/delete serializer and does not need info about students
class SectionNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('name', 'course', 'code')
        extra_kwargs = { 'code': { 'write_only': True } }




#serializer for indexing/creating a course and simultaneously creating sections
class CourseListCreateSerializer(serializers.ModelSerializer):
    
    sections = SectionNestedSerializer(many=True)
   
    class Meta:
        model = Course
        fields = ("name", "subject","teacher", "sections")
    
    #simultaneous creation of course and its related section will require a nested object coming from the client. The 'sections' object must be an interable The view is not customized to process the request appropriately. JSON should be sent according to the pattern {'sections': [{section feilds dict}, {'''}}, {'''}...'''}...], 'course':{course feilds dict}
    def create(self, validated_data):
        # pop out sections data
        sections_data = validated_data.pop('sections', None)
        course = Course.objects.create(**validated_data)
        if sections_data is not None:
            all_codes = Section.objects.values_list('code', flat=True)
            all_codes = list(all_codes)
            for section_data in sections_data:
                thing = generate_section_code(all_codes)
                section_data["code"] = generate_section_code(all_codes)
                section = Section.objects.create(course=course, **section_data)
                section.save()
        return course

#serializer for updating/deleting a course and seeing details. Section updated/deletion handled separately
class CourseRUDSerializer(serializers.ModelSerializer):
    sections = SectionNestedSerializer(many=True, read_only=True)
    students = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_students(self, obj):
        students = Student.objects.filter(class__course = obj)
        serialized_students = StudentSerializer(students, many=True)
        return serialized_students
        
         
        
        

    

        
        