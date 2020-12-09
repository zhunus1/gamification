# Generated by Django 3.1.4 on 2020-12-08 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('session_token', models.CharField(default=0, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='staff', serialize=False, to='users.user')),
                ('is_lecturer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to='users.user')),
                ('mbti', models.PositiveSmallIntegerField(choices=[('Analysts', ((1, 'Architect'), (2, 'Logician'), (3, 'Commander'), (4, 'Debater'))), ('Diplomats', ((1, 'Advocate'), (2, 'Mediator'), (3, 'Protagonist'), (4, 'Campaigner'))), ('Sentinels', ((1, 'Logistician'), (2, 'Defender'), (3, 'Executive'), (4, 'Consul'))), ('Explorers', ((1, 'Virtuoso'), (2, 'Adventurer'), (3, 'Entrepreneur'), (4, 'Entertainer')))])),
                ('english_level', models.PositiveSmallIntegerField(choices=[(1, 'Beginner'), (2, 'Elementary'), (3, 'Pre-Intermediate'), (4, 'Upper-Intermediate'), (5, 'Advanced')])),
                ('programming_exp', models.PositiveSmallIntegerField(choices=[(1, "I didn't program anything"), (2, 'I have basic knowledge'), (3, 'Know very well')])),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.staff')),
            ],
        ),
    ]
