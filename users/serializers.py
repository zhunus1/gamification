from rest_framework import serializers
from .models import User, Student, Staff

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',
                'password',
                'first_name',
                'last_name',
                'avatar',
        )

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'user',
            'lecturer',
            'teacher',
            'mbti',
            'english_level',
            'programming_exp'
        )
        extra_kwargs = {'password': {'write_only': True}}

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('__all__')

class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
