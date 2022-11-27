from rest_framework import serializers
from .models.assignment import Assignment
from .models.grade import Grade
from accounts.serializers import StudentSerializer

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

    