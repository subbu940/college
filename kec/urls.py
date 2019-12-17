from django.urls import path
from . import views
from .api import AppView, DepartmentView, StaffView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'kec'
urlpatterns = [
    path('', views.index, name='index'),
    path('application/', views.application, name='application'),
    path('stu_registration/', views.student_registration, name='stu-register'),
    path('staff_register/', views.staff_registration, name='staff-register'),
    path('student_login/', views.student_login, name='student_login'),
    path('staff_login/', views.staff_login, name='staff_login'),
    path('student_details/', views.student_details, name='student_details'),
    path('staff_details/', views.staff_details, name='staff_details'),
    path('staff_list/', views.staff_list, name='staff_list'),
    path('student_list/', views.student_list, name='student_list'),
    path('staff/', views.staff, name='staff'),
    path('students/', views.student, name='student'),
    path('apply/', AppView.as_view()),
    path('department/', DepartmentView.as_view()),
    path("staff_api/", StaffView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
urlpatterns = format_suffix_patterns(urlpatterns) 