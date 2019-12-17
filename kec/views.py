from django.shortcuts import render
from .models import StudentApplication, Department, Student, Staff
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import StudentApplicationForm, UserCreationForm, StaffForm



def index(request):
    return render(request, 'kec/index.html')


def application(request):
    if request.method == 'POST':
        application_form = StudentApplicationForm(request.POST)
        if application_form.is_valid():
            application_form.save()
            return HttpResponseRedirect('/kec/')

        # StudentApplication.objects.create(
        #     student_name=request.POST['student_name'],
        #     email=request.POST['email'],
        #     ssc_percentage=request.POST['ssc_percentage'],
        #     inter_percentage=request.POST['inter_percentage'])
        # return HttpResponseRedirect('/kec/')
    # return render(request, 'kec/application.html')
    else:
        application_form = StudentApplicationForm()
    return render(request, 'kec/application.html', {'form': application_form})


def student_registration(request):
    if request.method == 'POST':
        student = StudentApplication.objects.filter(email=request.POST['email'], is_verified=True)
        if not student.exists():
            return render(request, "kec/application.html", {"error": "Apply and Register."})
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        department = Department.objects.get(department_name =request.POST['department'])
        Student.objects.create(
            student_name=request.POST['student_name'],
            dob=request.POST['dob'],
            father_name=request.POST['father_name'],
            mother_name=request.POST['mother_name'],
            mobile_no=request.POST['mobile_no'],
            gender=request.POST['gender'],
            student_image=request.FILES['student_image'],
            student_application=student.first(),
            department=department,
            user=user
        )
        return HttpResponseRedirect('/kec/')
    return render(request, 'kec/student_registration.html')


def staff_registration(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        staff_form = StaffForm(request.POST and request.FILES)
        form = user_form and staff_form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/kec/')

    #     user = User.objects.create_user(
    #         username=request.POST['username'],
    #         password=request.POST['password'],
    #         email=request.POST['email']
    #     )
    #     department = Department.objects.get(department_name=request.POST['department'])
    #     Staff.objects.create(
    #         staff_name=request.POST['staff_name'],
    #         mobile_no=request.POST['mobile_no'],
    #         experience=request.POST['experience'],
    #         specialization=request.POST['specialization'],
    #         gender=request.POST['gender'],
    #         department=department,
    #         staff_image=request.FILES['staff_image'],
    #         user=user
    #     )
    #     return HttpResponseRedirect('/kec/')
    # return render(request, 'kec/staff_register.html')
    else:
        form = UserCreationForm and StaffForm
    return render(request, 'kec/staff_register.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/kec/student_details/')
        else:
            return render(request, 'kec/student_login.html', {'error_message': 'Invalid Credentials'})
    return render(request, 'kec/student_login.html')


def staff_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/kec/staff_details')
        else:
            return render(request, 'kec/staff_login.html', {'error_message': 'Invalid Credentials'})
    return render(request, 'kec/staff_login.html')


def student_details(request):
    student = request.user.student
    return render(request, 'kec/student_details.html', {'student': student})


def staff_details(request):
    staff = request.user.staff
    return render(request, 'kec/staff_details.html', {'staff': staff})


def staff_list(request):
    staf_list = Staff.objects.filter(department= request.user.student.department)
    return render(request, 'kec/staff_list.html', {'staf_list': staf_list})


def student_list(request):
    stu_list = Student.objects.filter(department=request.user.staff.department)
    return render(request, 'kec/student_list.html', {'stu_list': stu_list})


def staff(request):
    sta = Staff.objects.order_by('id')
    return render(request, 'kec/staff.html', {'sta': sta})


def student(request):
    stu = Student.objects.order_by('-department_id')
    return render(request, 'kec/student.html', {'stu': stu})


