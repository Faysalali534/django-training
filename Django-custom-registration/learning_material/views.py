from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Course, Lesson


# Create your views here.

class CourseListView(ListView):
    template_name = 'learning_material/course_list_view.html'
    model = Course
    context_object_name = 'courses'
