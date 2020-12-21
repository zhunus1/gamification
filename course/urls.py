from django.urls import path,include
from .views import CourseListAPIView,ModuleListAPIView,QuestionAPIView,CodingAPIView,ProjectAPIView
urlpatterns = [
    path('',CourseListAPIView.as_view()),
    path('modules/',ModuleListAPIView.as_view()),
    path('question/',QuestionAPIView.as_view()),
    path('coding/submit',CodingAPIView.as_view()),
    path('project/submit',ProjectAPIView.as_view()),
]
