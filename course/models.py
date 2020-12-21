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

class Filling(models.Model):
    question = models.TextField()
    description = models.TextField()

class Quiz(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='project')
    coding = models.OneToOneField(Coding, on_delete=models.CASCADE, related_name='project')
    filling = models.OneToOneField(Filling, on_delete=models.CASCADE, related_name='project')

class Contest(models.Model):
    coding = models.ManyToManyField(
        Coding,
    )

class Project(models.Model):
    description = models.TextField()
    attachement = models.FileField(upload_to ='attachements/',null=True,blank=True)

class Theory(models.Model):
    name = models.CharField(max_length=255)
    question = models.ManyToManyField(
        Question,
    )
    video_url = models.URLField(blank=True, null=True)
    attachement = models.FileField(upload_to ='attachements/',null=True,blank=True)

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
        on_delete=models.CASCADE
    )
    project = models.OneToOneField(Project, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=255)
    module = models.ManyToManyField(
        Module,
    )
    lector = models.ManyToManyField(
        Lecturer,
    )
    practicer = models.ManyToManyField(
        Practicer,
    )
