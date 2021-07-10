from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from vaccine.models import Vaccination
from profiles.models import Profile

def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

def index(request):
    if request.user.is_authenticated:
        if is_patient(request.user):
            return HttpResponseRedirect('patient/afterlogin')
        else:
            return redirect('admin-dashboard')
    return render(request, 'vaccine/index.html')
def is_superuser(id):
    try:
        user= User.objects.filter(id=id).values_list('is_superuser', flat=True)
        if user[0]:
            return True
        else:
            return False
    except Exception as e:
        return False


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    val=  is_superuser(request.user.id)
    if val:
        dict={
        'total_p' : Profile.objects.filter().count(),
        'total_p_vaccineation' : Vaccination.objects.filter(First_Status='Pending').count(),
        'total_c_vaccineation': Vaccination.objects.filter(First_Status='Completed').count()
        }
        return render(request,'vaccine/admin_dashboard.html',dict)
    else:
        return render(request, 'patient/patient_dashboard.html')

@login_required(login_url='patient:login')
def pendingpatient(request):
    val = is_superuser(request.user.id)
    if val:
        p_list = Vaccination.objects.filter(First_Status='Pending')
        return render(request, 'patient/pending_patient.html',{'p_list':p_list})
    else:
        return render(request, 'patient/patient_dashboard.html')

@login_required(login_url='patient:login')
def completedpatient(request):
    val = is_superuser(request.user.id)
    if val:
        c_list = Vaccination.objects.filter(First_Status='Completed')
        return render(request, 'patient/completed_patient.html',{'c_list':c_list})
    else:
        return render(request, 'patient/patient_dashboard.html')
