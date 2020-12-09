from django.urls import path
from .views import CreateUserAPIView,CreateStudentAPIView,CreateStaffAPIView,authenticate_user

urlpatterns = [
    path('create/user/',CreateUserAPIView.as_view()),
    path('create/student/',CreateStudentAPIView.as_view()),
    path('create/staff/',CreateStaffAPIView.as_view()),
    path('auth/',authenticate_user),
]
