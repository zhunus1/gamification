# Generated by Django 3.1.4 on 2020-12-21 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('note', models.TextField()),
                ('input_example', models.CharField(max_length=255)),
                ('output_example', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Filling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('attachement', models.FileField(blank=True, null=True, upload_to='attachements/')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('hint', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('video_url', models.URLField(blank=True, null=True)),
                ('attachement', models.FileField(blank=True, null=True, upload_to='attachements/')),
                ('question', models.ManyToManyField(to='course.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coding', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='course.coding')),
                ('filling', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='course.filling')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='course.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='variant',
            field=models.ManyToManyField(to='course.Variant'),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('module_progress', models.FloatField(default=0.0)),
                ('contest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.contest')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.project')),
                ('quiz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.quiz')),
                ('theory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.theory')),
            ],
        ),
    ]
