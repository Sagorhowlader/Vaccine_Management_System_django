import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .form import UserRegisterForm, ProfileForm
from django.contrib.auth.models import Group, User
from vaccine.forms import VaccinetionForm , EditVaccinetionForm
from .models import Profile
from vaccine.models import Vaccine, Vaccination ,Payment

def formDateValidation(request, sDate, eDate, url, uid = None):
    if not sDate:
        return render(request, url, {'flag': '1', 'formValidation': 'Select Start Date'})

    if not eDate:
        return render(request, url, {'flag': '1', 'formValidation': 'Select End Date'})


    dateTime_sDate = datetime.datetime.strptime(sDate, '%Y-%m-%d')
    dateTime_eDate = datetime.datetime.strptime(eDate, '%Y-%m-%d')

    if (dateTime_eDate - dateTime_sDate).days < 0:
        return render(request, url,
                      {'flag': '1', 'formValidation': 'Please Select A Valid Date Range'})

    return 'valid'

def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


def afterlogin_view(request):
    if is_patient(request.user):
        return redirect('patient:patient-dashboard')


class SignUp(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        user = form.save(commit=False)
        user.save()
        user_group = Group.objects.get_or_create(name='PATIENT')
        user_group[0].user_set.add(user)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


@login_required(login_url='patient:login')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    total = Vaccination.objects.filter(
        First_Status='Pending'
    ) | Vaccination.objects.filter(
    Second_Status='Pending'
    )
    dict = {

       'total':total,
        'vaccination':Vaccination.objects.filter(User=request.user,Second_Status='Pending')
    }
    return render(request, 'patient/patient_dashboard.html',dict)

def edit_vaccine(request,id):
    vaccination=Vaccination.objects.get(id=id)
    form = EditVaccinetionForm(request.POST or None,instance=vaccination)
    if form.is_valid():
        form.save()
        return redirect('patient:patient-dashboard')
    return render(request,'vaccine/edit_vaccine.html',{'form':form})
@login_required(login_url='patient:login')
@user_passes_test(is_patient)
def makeappointment(request):
    return render(request, 'patient/makeappointment.html')


@login_required(login_url='patient:login')
@user_passes_test(is_patient)
def Create_Profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
        if request.method == 'POST':
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('vaccine:vaccine_warring')

        return render(request, 'patient/create_profile.html', {'form': form,'profile': profile})

    except Exception as e:
        return render(request, 'patient/create_profile.html', {'form': form,'profile': profile})
@login_required(login_url='patient:login')
@user_passes_test(is_patient)
def create_schedule(request):
    try:
        time = datetime.datetime.now() + datetime.timedelta(days=90)
        form = VaccinetionForm()
        if request.method == 'POST':
            form = VaccinetionForm(request.POST)
            if form.is_valid():
                t = form.save(commit=False)
                t.User = request.user
                t.Second_schdule = time
                price = Vaccine.vaccine_price(Vaccine, form.cleaned_data['Vaccine_name'])
                t.Price = price
                form.save()
                id = Vaccine.vaccine_id(Vaccine, form.cleaned_data['Vaccine_name'])
                return redirect('vaccine:payment',id)
        return render(request, 'patient/create_schedule.html', {'form': form})
    except Exception as e:
        print(e)


class ListViewPatient(generic.ListView):
    model = Profile
    template_name = 'patient/patient_list_view.html'

def payment_report(request):
    try:
        if request.POST.get('reportform') == 'reportformvalue':
            form_sDate = (request.POST.get('sdate'))
            form_eDate = (request.POST.get('edate'))
        else:
            form_sDate=datetime.datetime.today().strftime('%Y-%m-%d')
            form_eDate=(datetime.datetime.now() + datetime.timedelta(days=7)).date()
        payment = Payment.objects.filter(Date__range=[form_sDate, form_eDate])
        dict = {
            'payments':payment,
            'sdate':form_sDate,
            'edate':form_eDate
        }
        return render(request,'vaccine/payment_report.html',dict)
    except Exception as e:
        print(e)
def patient_delete(request, id):
    try:
        obj = Profile.objects.get(user_id=id)
        obj.delete()
        v_obj = Vaccination.objects.get(User_id=id)
        v_obj.delete()
        return redirect('patient:patient_list_view')
    except Exception as e:
        return redirect('patient:patient_list_view')

def deleted_vaccine(request,id):
    vaccination=Vaccination.objects.get(id=id)
    vaccination.delete()
    return redirect('patient:patient-dashboard')

def vaccine_report(request,pk):
    dict={
        'profile':Profile.objects.get(user=request.user),
        'vaccine':Vaccination.objects.get(id=pk)
    }
    return render(request,'patient/print_form.html',dict)