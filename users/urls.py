from django.urls import path
from .views import CreateStudentAPIView,authenticate_user

urlpatterns = [
    path('create/student/',CreateStudentAPIView.as_view()),
    path('auth/',authenticate_user),
]
