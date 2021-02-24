from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_professor = models.BooleanField(default=False)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', primary_key=True)
    phone_number = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    student = 'student'
    professor = 'professor'
    user_types = [
        (student, 'student'),
        (professor, 'professor'),
    ]
    user_type = models.CharField(max_length=9, choices=user_types, default=student)

    def __str__(self):
        return self.user.username

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     phone_number = models.CharField(max_length=30)
#     location = models.CharField(max_length=30)
#     student = 'student'
#     professor = 'professor'
#     user_type = [
#         (student, 'student'),
#         (professor, 'professor'),
#     ]
#     user_type = models.CharField(max_length=9, choices=user_type, default=student)


# class Professor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     phone_number = models.CharField(max_length=30)
#     designation = models.CharField(max_length=30)



