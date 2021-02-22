from django.urls import path
from .import views

urlpatterns = [
     path('', views.index_page, name='index'),
     path('accounts/register/', views.register, name='register'),
     path('accounts/student_register/', views.student_register.as_view(), name='student_register'),
     path('accounts/professor_register/', views.student_register.as_view(), name='professor_register'),
     path('accounts/login/', views.login_request, name='login_request'),
     path('accounts/logout/', views.logout_view, name='logout'),
]