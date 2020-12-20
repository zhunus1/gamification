from django.db import models
from users.models import Student, Lecturer, Practicer
# Create your models here.


class Variant(models.Model):
    title = models.CharField(max_length=255)
    is_correct = models.BooleanField()

class Question(models.Model):
    question = models.TextField()
    variant = models.ManyToManyField(
        Variant,
    )
    hint = models.TextField()

class Coding(models.Model):
    question = models.TextField()
    note = models.TextField()
    input_example = models.CharField(max_length=255)
    output_example = models.CharField(max_length=255)
    answer = models.TextField()

class Filling(models.Model):
    question = models.TextField()
    description = models.TextField()
    answer = models.TextField()

class Quiz(models.Model):
    grade = models.FloatField(default=0.0)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='project')
    coding = models.OneToOneField(Coding, on_delete=models.CASCADE, related_name='project')
    filling = models.OneToOneField(Filling, on_delete=models.CASCADE, related_name='project')

class Contest(models.Model):
    grade = models.FloatField(default=0.0)
    coding = models.ManyToManyField(
        Coding,
    )

class Attachement(models.Model):
    attachement = models.FileField(upload_to ='attachements/')

class Project(models.Model):
    grade = models.FloatField(default=0.0)
    description = models.TextField()
    attachement = models.ManyToManyField(
        Attachement,
    )

class Theory(models.Model):
    grade = models.FloatField(default=0.0)
    name = models.CharField(max_length=255)
    question = models.ManyToManyField(
        Question,
    )
    video_url = models.URLField(blank=True, null=True)
    attachement = models.ManyToManyField(
        Attachement,
    )

class Module(models.Model):
    name = models.CharField(max_length=255)
    module_progress = models.FloatField(default=0.0)
    theory = models.OneToOneField(
        Theory,
        on_delete=models.CASCADE,
    )
    quiz = models.OneToOneField(
        Quiz,
        on_delete=models.CASCADE,
    )
    contest = models.OneToOneField(
        Contest,
        on_delete=models.CASCADE,
    )
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='project')

class Course(models.Model):
    module = models.ManyToManyField(
        Module,
    )
    lector = models.ManyToManyField(
        Lecturer,
    )
    practicer = models.ManyToManyField(
        Practicer,
    )
