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


#section list and create serializer
class SectionListCreateSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    class Meta:
        model = Section
        fields = "__all__"
        extra_kwargs = {
            'students': {'read_only': True},
            'code': {"read_only": True},
        }
    #custom creation to automatically generate code and set course w/o needing client to explicitly do so.
    def create(self, validated_data):
        validated_data["course_id"] = self.context.get('view').kwargs["course_id"]
        all_codes = Section.objects.values_list('code', flat=True)
        validated_data["code"] = generate_section_code(all_codes)
        section = Section.objects.create(**validated_data)
        section.save()
        return section
    
    
#section detail serializer will have student data on a per section basis
class SectionRUDSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    students = StudentSerializer(many=True)
    teacher = serializers.SerializerMethodField()
    class Meta:
        model = Section
        fields = ("name", "teacher", "students", "course","code")
    
    def get_teacher(self,obj):
        return obj.course.teacher.__str__()

#serializer for student view of their sections
class StudentSectionListSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    course = serializers.StringRelatedField()
    class Meta:
        model = Section
        fields = ("name", "teacher", "course")
    def get_teacher(self,obj):
        return obj.course.teacher.__str__()

#serializer for indexing/creating a course and simultaneously creating sections
class CourseListCreateSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()
    sections = SectionNestedSerializer(many=True, write_only=True)
    class Meta:
        model = Course
        fields = ("name", "subject","teacher", "sections", "id")
    
    
    #simultaneous creation of course and its related section will require a nested object coming from the client. The 'sections' object must be an interable The view is not customized to process the request appropriately. JSON should be sent according to the pattern {'sections': [{section feilds dict}, {'''}}, {'''}...'''}...], 'course':{course feilds dict}
    def create(self, validated_data):
        # pop out sections data
        sections_data = validated_data.pop('sections', None)
        course = Course.objects.create(**validated_data)
        if sections_data is not None:
            all_codes = Section.objects.values_list('code', flat=True)
            all_codes = list(all_codes)
            for section_data in sections_data:
                section_data["code"] = generate_section_code(all_codes)
                section = Section.objects.create(course=course, **section_data)
                section.save()
        return course

#serializer for updating/deleting a course and seeing details. Section updated/deletion handled separately
class CourseRUDSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()
    sections = SectionNestedSerializer(many=True, read_only=True)
    students = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_students(self, obj):
        student_ids = obj.sections.values_list('students', flat=True)
        students = []
        for id in student_ids:
            student = Student.objects.get(pk=id)
            students.append(student)
        serialized_students = StudentSerializer(students, many=True)
        return serialized_students.data


    
    
        

        
         
        
        

    

        
        