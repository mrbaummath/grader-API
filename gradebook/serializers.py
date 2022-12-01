from rest_framework import serializers
from .models.assignment import Assignment
from .models.grade import Grade
from accounts.serializers import StudentSerializer
from accounts.models.student import Student
from classes.models.course import Course


class AssignmentSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    class Meta:
        model = Assignment
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data["course_id"] = self.context.get('view').kwargs["course_id"]
        assignment = assignment.create(**validated_data)
        assignment.save()
        return assignment



class GradeSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    assignment = AssignmentSerializer()
    class Meta:
        model= Grade
        fields = '__all__'

class GradebookEntrySerializer(serializers.ModelSerializer):
    assignment = serializers.StringRelatedField()
    
    class Meta:
        model = Grade
        fields = ('id','assignment', 'value')

class CourseGradesByStudentSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    course_graded_assignments = serializers.SerializerMethodField()
    
    class Meta:
        model = Student
        fields = ('id', 'student', 'course_graded_assignments')
        
    def get_student(self, obj):
        return obj.__str__()
        
    def get_course_graded_assignments(self, obj):
        Student.objects.prefetch_related('grades')
        course_id = self.context.get('view').kwargs["course_id"]
        grades = obj.grades.filter(course=course_id)
        serialized_grades = GradebookEntrySerializer(grades, many=True)
        return serialized_grades.data
    

    
  
    