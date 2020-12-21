from django.shortcuts import render
from rest_framework import generics
from .models import (
    Course,
    Module,
    Question,
    Coding,
    Contest
)
from users.models import Student,StudentContest
from .serializers import (
    CourseSerializer,
    ModuleSerializer,
    QuestionViewSerializer,
    VariantSerializer,
    CodingSubmitSerializer
)
from users.authentication import GamificationAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import exceptions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.

#API for retrieving whole course
class CourseListAPIView(generics.ListAPIView):
    authentication_classes = (GamificationAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#API for retrieving module informations
class ModuleListAPIView(generics.ListAPIView):
    authentication_classes = (GamificationAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

#API for quiz(Question type)
#Here you send me id of question and I return you its correct variant
class QuestionAPIView(APIView):
    authentication_classes = (GamificationAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        serializer = QuestionViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question_id = serializer.validated_data['question_id']
        question = get_object_or_404(Question,id=question_id)
        variants = VariantSerializer(question.variant,many=True)
        for variant in variants.data:
            if variant['is_correct'] is True:
                return Response(variant,status=status.HTTP_200_OK)

#API for Submitting Coding (Contest,Quiz)
class CodingAPIView(APIView):
    authentication_classes = (GamificationAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        user = request.user
        serializer = CodingSubmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        coding = get_object_or_404(Coding,pk=serializer.validated_data['coding_id'])
        contest = Contest.objects.create(coding=coding)
        contest = StudentContest.objects.create(contest=contest,answer=serializer.validated_data['answer'])
        return Response(contest.data,status=status.HTTP_200_OK)

#API for Submitting Coding (Contest,Quiz)
class ProjectAPIView(APIView):
    authentication_classes = (GamificationAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        user = request.user
        serializer = CodingSubmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        coding = get_object_or_404(Coding,pk=serializer.validated_data['coding_id'])
        contest = Contest.objects.create(coding=coding)
        contest = StudentContest.objects.create(contest=contest,answer=serializer.validated_data['answer'])
        return Response(contest.data,status=status.HTTP_200_OK)
