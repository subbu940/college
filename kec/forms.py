from django.forms import ModelForm
from .models import StudentApplication, Student, Staff
from django.contrib.auth.models import User


class StudentApplicationForm(ModelForm):

    class Meta:
        model = StudentApplication
        fields = '__all__'
        exclude = ['is_verified']


class UserCreationForm(ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['first_name', 'last_name']


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['ssc_percentage', 'inter_percentage']


class StaffForm(ModelForm):

    class Meta:
        model = Staff
        fields = '__all__'
