from rest_framework import serializers
from .models import User, Student, Lecturer, Practicer

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
    user = UserSerializer()
    class Meta:
        model = Student
        fields = (
            'user',
            'lecturer',
            'practicer',
            'mbti',
            'english_level',
            'programming_exp'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data['user'])
        validated_data['user'] = user
        student = Student.objects.create(**validated_data)
        return student

class LectorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Lecturer
        fields = ('user',)

class PracticerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Practicer
        fields = ('user',)

class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
