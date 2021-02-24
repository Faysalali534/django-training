from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from django.contrib.auth.models import User
from .models import UserInfo


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password'
        }


class UserInfoForm(forms.ModelForm):
    phone_number = forms.CharField(required=False)
    location = forms.CharField(required=False)
    student = 'student'
    professor = 'professor'
    user_types = [
        (student, 'student'),
        (professor, 'professor'),
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta:
        model = UserInfo
        fields = ('phone_number', 'location', 'user_type')


# class StudentSignUpForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     phone_number = forms.CharField(required=True)
#     location = forms.CharField(required=True)
#     student = 'student'
#     professor = 'professor'
#     user_type = [
#         (student, 'student'),
#         (professor, 'professor'),
#     ]
#     user_type = forms.ChoiceField(required=True, choices=user_type)
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_student = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         student = Student.objects.create(user=user)
#         student.phone_number = self.cleaned_data.get('phone_number')
#         student.location = self.cleaned_data.get('location')
#         student.user_type = forms.CharField(widget=forms.Select)
#         print(student.user_type)
#         student.save()
#         return user
#
#
# class ProfessorSignUpForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     phone_number = forms.CharField(required=True)
#     designation = forms.CharField(required=True)
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('first_name', 'last_name', 'phone_number')
#         print(Professor._meta.fields)
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_professor = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.save()
#         professor = Professor.objects.create(user=user)
#         professor.phone_number = self.cleaned_data.get('phone_number')
#         # student.location = self.cleaned_data.get('location')
#         professor.save()
#         return user
