from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import StudentSignUpForm, ProfessorSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


def register(request):
    return render(request, 'accounts/register.html', {})


def index_page(request):
    return render(request, 'accounts/index.html', {})


class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class professor_register(CreateView):
    model = User
    form_class = ProfessorSignUpForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
# class employee_register(CreateView):
#     model = User
#     form_class = EmployeeSignUpForm
#     template_name = '../templates/employee_register.html'
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'accounts/login.html', context={'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')
