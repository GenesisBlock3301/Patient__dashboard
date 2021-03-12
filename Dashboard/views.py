from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .models import Patient
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import User
from django.contrib.auth import login, authenticate
from django.db.models import Q


# Create your views here.

class DashboardView(View):
    def get(self, request):
        patients = Patient.objects.all()
        # search patient with patient Grade
        grade = request.GET.get('q')
        if grade:
            patients = Patient.objects.filter(
                Q(grade__icontains=grade)
            ).distinct()
        page = request.GET.get('page', 1)
        # every page have two record
        pagination = Paginator(patients, per_page=2)
        try:
            patients = pagination.page(page)
        except PageNotAnInteger:
            patients = pagination.page(1)
        except EmptyPage:
            patients = Paginator.page(pagination.num_pages)
        # print(patients.next_page_number())
        return render(request, 'dashboard.html', {'patients': patients})


# patient add form
class PatientFormView(View):
    def get(self, request):
        user = request.user
        # print(">>>>>>>>>>>>>>>>>>", user)
        if user.is_authenticated:
            try:
                patient = Patient.objects.get(patients=user)
            except Patient.DoesNotExist:
                patient = Patient.objects.create(patients=user, name='', age=0, weight=0, retina_image='', grade=0)
            return render(request, 'PatientForm.html', {'patient': patient})
        else:
            return redirect('login')

    def post(self, request):
        name = request.POST['name']
        age = request.POST['age']
        weight = request.POST['weight']
        retina_image = request.FILES['file']
        grade = request.POST['grade']
        if request.user and name and age and weight and retina_image and grade:
            # print(">>>>>>>>>>>>>image", retina_image)
            patient = Patient.objects.get(patients=request.user)
            # patient.user = request.user
            patient.name = name
            patient.age = age
            patient.weight = weight
            patient.retina_image = retina_image
            patient.grade = grade
            patient.save()
            # messages.success(request, "Patient information successfully created")
            return redirect('form')
        else:
            messages.error(request, 'Please fill the all filed here')
        print(name, age, weight, retina_image, grade)
        return render(request, 'PatientForm.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # postData = request.POS
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # validation
        # print(">>>>>>>>>>>>>>>>>>>>>>>", email, )
        # error_message = None
        if password == password2:
            user = User.objects.filter(email=email)
            if user.exists():
                messages.error(request, "User already exists")
                return redirect('register')
            else:
                user = User(username=username, email=email)
                user.set_password(password)
                messages.success(request, "Successfully account created")
                user.save()
        else:
            messages.error(request, "Password not match")
        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        # print("Username", username)
        # authenticate user
        user = authenticate(username=username, password=password)
        # print(user)
        if user:
            login(request, user)
            # print("Success>>>>>>>>>>>>>>>>>>>>>")
            return redirect('form')
        # print("Success>>>>>>>>>>>>>>>>>>>>>")
        return render(request, 'login.html')
