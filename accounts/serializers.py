from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 1 } }

class UserSignupSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    username = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)
    is_teacher = serializers.BooleanField()
    is_student = serializers.BooleanField()

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
        return data
    
    def create(self, validated_data):
        del validated_data["password_confirmation"]
        return User.objects.create_user(**validated_data)