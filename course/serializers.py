from rest_framework import serializers
from .models import (
        Variant,
        Question,
        Coding,
        Filling,
        Quiz,
        Contest,
        Project,
        Theory,
        Module,
        Course,
)
from users.serializers import LectorSerializer,PracticerSerializer
class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):
    variant = VariantSerializer(many=True)
    class Meta:
        model = Question
        fields = (
            'id',
            'question',
            'variant',
            'hint',
        )

class CodingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coding
        fields = ('__all__')

class FillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filling
        fields = ('__all__')

class QuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    coding = CodingSerializer()
    filling = FillingSerializer()
    class Meta:
        model = Quiz
        fields = (
            'grade',
            'question',
            'coding',
            'filling',
        )

class ContestSerializer(serializers.ModelSerializer):
    coding = CodingSerializer(many=True)
    class Meta:
        model = Contest
        fields = (
            'grade',
            'coding',
        )

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'grade',
            'description',
            'attachement',
        )

class TheorySerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)
    class Meta:
        model = Theory
        fields = (
            'grade',
            'name',
            'question',
            'video_url',
            'attachement'
        )

class ModuleSerializer(serializers.ModelSerializer):
    theory = TheorySerializer()
    quiz = QuizSerializer()
    contest = ContestSerializer()
    project = ProjectSerializer()
    class Meta:
        model = Module
        fields = (
            'name',
            'module_progress',
            'theory',
            'quiz',
            'contest',
            'project',
        )

class CourseSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(many=True)
    lector = LectorSerializer(many=True)
    practicer = PracticerSerializer(many=True)
    class Meta:
        model = Course
        fields = (
            'name',
            'module',
            'lector',
            'practicer',
        )

class QuestionViewSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    class Meta:
        fields = ('question_id',)

class CodingSubmitSerializer(serializers.Serializer):
    answer = serializers.CharField()
    coding_id = serializers.IntegerField()
    class Meta:
        fields = ('answer','coding_id')
