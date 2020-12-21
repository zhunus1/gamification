from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    token = None
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Practicer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class StudentQuiz(models.Model):
    quiz = models.OneToOneField('course.Quiz', on_delete=models.CASCADE, primary_key=True)
    grade = models.FloatField(default=0.0)
    answer = models.IntegerField()

class StudentContest(models.Model):
    contest = models.OneToOneField('course.Contest', on_delete=models.CASCADE, primary_key=True)
    grade = models.FloatField(default=0.0)
    answer = models.TextField()

class StudentProject(models.Model):
    project = models.OneToOneField('course.Project', on_delete=models.CASCADE, primary_key=True)
    grade = models.FloatField(default=0.0)
    answer = models.TextField()


class Student(models.Model):
    ENGLISH_LEVEL = (
      (1, 'Beginner'),
      (2, 'Elementary'),
      (3, 'Pre-Intermediate'),
      (4, 'Upper-Intermediate'),
      (5, 'Advanced'),
    )
    PROGRAMMING_EXPERIENCE = (
      (1, "I didn't program anything"),
      (2, 'I have basic knowledge'),
      (3, 'Know very well'),
    )
    MBTI_TYPE = (
        ('Analysts', (
            (1, 'Architect'),
            (2, 'Logician'),
            (3, 'Commander'),
            (4, 'Debater'),
        )),
        ('Diplomats', (
            (1, 'Advocate'),
            (2, 'Mediator'),
            (3, 'Protagonist'),
            (4, 'Campaigner'),
        )),
        ('Sentinels', (
            (1, 'Logistician'),
            (2, 'Defender'),
            (3, 'Executive'),
            (4, 'Consul'),
        )),
        ('Explorers', (
            (1, 'Virtuoso'),
            (2, 'Adventurer'),
            (3, 'Entrepreneur'),
            (4, 'Entertainer'),
        )),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student', primary_key=True)

    lecturer = models.ForeignKey(
        Lecturer,
        on_delete=models.CASCADE,
    )

    practicer = models.ForeignKey(
        Practicer,
        on_delete=models.CASCADE,
    )

    quizes = models.ForeignKey(StudentQuiz, on_delete=models.CASCADE)
    projects = models.ForeignKey(StudentProject, on_delete=models.CASCADE)
    contests = models.ForeignKey(StudentContest, on_delete=models.CASCADE)


    mbti = models.PositiveSmallIntegerField(choices=MBTI_TYPE)
    english_level = models.PositiveSmallIntegerField(choices=ENGLISH_LEVEL)
    programming_exp = models.PositiveSmallIntegerField(choices=PROGRAMMING_EXPERIENCE)
