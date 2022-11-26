from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models.teacher import Teacher
from .models.student import Student

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 1 } }

class UserSignupSerializer(serializers.Serializer):
    # Fields needed for both user and teacher/student creation
    first_name = serializers.CharField(max_length=100, write_only=True)
    last_name = serializers.CharField(max_length=100, write_only=True)
    title = serializers.CharField(max_length=20, write_only=True, required=False)
    pronouns = serializers.CharField(max_length=100, write_only=True)
    year_in_school = serializers.ChoiceField([
        ("N/A", "Not Applicable"),
        ("FR", "First Year"),
        ("SO", "Sophomore"),
        ("JR", "Junior"),
        ("SR", "Senior"),
    ], write_only=True, required=False)
    email = serializers.CharField(max_length=50, required=True)
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(required=True, write_only = True)
    password_confirmation = serializers.CharField(required=True, write_only=True)
    is_teacher = serializers.BooleanField()
    is_student = serializers.BooleanField()

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')
        #Ensure user is either a teacher or a student 
        if data['is_teacher'] == False and data['is_student'] == False:
            raise serializers.ValidationError('Please select an account type')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
        return data
    
    def create(self, validated_data):
        del validated_data["password_confirmation"]
        #pop out arguments not needed for creating the user model. THese will be used to instantiate either a teacher or a student as needed
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        pronouns = validated_data.pop("pronouns")
        title = validated_data.pop("title", None)
        year_in_school = validated_data.pop("year_in_school", None)
        # create the user
        user = User.objects.create_user(**validated_data)
        account_data = {
            "first_name": first_name,
            "last_name": last_name,
            "pronouns": pronouns,
            "user": user
        }
        if user.is_teacher:
            account_data["title"] = title
            teacher = Teacher.objects.create(**account_data)
            user.groups.add(1)
            teacher.save()
        elif user.is_student:
            account_data["year"] = year_in_school
            student = Student.objects.create(**account_data)
            user.groups.add(2)
            student.save()
        return user

class TeacherSerializer(serializers.ModelSerializer):
    
    email = serializers.SerializerMethodField()
    full_title = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = ("first_name", "last_name", "email", "full_title", "pronouns")
    
    def get_email(self, obj):
        user = UserSerializer(obj.user)
        return user.data["email"]
    
    def get_full_title(self, obj):
        return obj.__str__()
        


class StudentSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "pronouns", "year_in_school", "email")
    
    def get_email(self, obj):
        user = UserSerializer(obj.user)
        return user.data["email"]
        
