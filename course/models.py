from django.db import models
from users.models import Student
# Create your models here.


class Variant(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField()

class Question(models.Model):
    question = models.TextField()
    variants = models.ForeignKey(
        'Variant',
        on_delete=models.CASCADE,
    )
    hint = models.TextField()

class Coding(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=255)
    hint = models.TextField()

class Example(models.Model):
    input = models.CharField(max_length=255)
    output = models.CharField(max_length=255)

class Filling(models.Model):
    question = models.TextField()
    examples = models.OneToOneField(Example, on_delete=models.CASCADE, related_name='examples')
    note = models.TextField()
    answer = models.TextField()

class Quiz(models.Model):
    grade = models.FloatField(default=0.0)
    test = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='project')
    coding = models.OneToOneField(Coding, on_delete=models.CASCADE, related_name='project')
    filling = models.OneToOneField(Filling, on_delete=models.CASCADE, related_name='project')

class Contest(models.Model):
    grade = models.FloatField(default=0.0)
    codings = models.ForeignKey(
        'Coding',
        on_delete=models.CASCADE,
    )

class Project(models.Model):
    grade = models.FloatField(default=0.0)
    description = models.TextField()

class Theory(models.Model):
    grade = models.FloatField(default=0.0)
    name = models.CharField(max_length=255)
    questions = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
    )
    video_url = models.URLField(blank=True, null=True)
    attachements = models.FileField(upload_to ='attachements/')

class Module(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    module_progress = models.FloatField(default=0.0)
    theory = models.ForeignKey(
        'Theory',
        on_delete=models.CASCADE,
    )
    quiz = models.ForeignKey(
        'Quiz',
        on_delete=models.CASCADE,
    )
    contest = models.ForeignKey(
        'Contest',
        on_delete=models.CASCADE,
    )
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='project')
