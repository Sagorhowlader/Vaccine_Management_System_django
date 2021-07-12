from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from .forms import VaccineForm, PaymentForm
from .models import Vaccine


def vaccine_list(request):
    vaccines = Vaccine.objects.all()
    return render(request, 'vaccine/vaccine_list.html', {'vaccines': vaccines})


class DetailsVaccine(generic.DetailView):
    model = Vaccine
    template_name = 'vaccine/vaccine_details.html'


def vaccine_search(request):
    text = request.POST['search']
    print(text)
    return render(request, 'vaccine/vaccine_list.html')


class ListViewVaccine(generic.ListView):
    model = Vaccine
    template_name = 'vaccine/vaccine_list_view.html'

class ListViewVaccineAfter(generic.ListView):
    model = Vaccine
    template_name = 'patient/after_vaccine_list.html'

def add_vaccine(request):
    form = VaccineForm()
    try:
        if request.method == 'POST':

            form = VaccineForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('vaccine:vaccine_list_view')
        return render(request, 'vaccine/add_vaccine.html', {'form': form})
    except Exception as e:
        return render(request, 'vaccine/add_vaccine.html', {'form': form})


def delete_vaccine(request, id):
    obj = Vaccine.objects.get(Vaccine_Id=id)
    obj.delete()
    return redirect('vaccine:vaccine_list_view')


def vaccine_warring(request):
    return render(request, 'vaccine/warning.html')


def registration_successfully(request):
    return render(request, 'vaccine/registration_successfully.html')


def vaccine_payment(request,id):
    try:
        vaccine = Vaccine.objects.get(id=id)
        total = int(vaccine.Vaccine_price)+ 1500
        form = PaymentForm()
        dict = {
            'vaccine_id' : vaccine.id,
            'vaccine_name': vaccine.Vaccine_name,
            'vaccine_price': vaccine.Vaccine_price,
            'vaccine_image': vaccine.Vaccine_image,
            'total':total,
            'form':form
        }
        if request.POST:

            form = PaymentForm(request.POST)

            if form.is_valid():
                payment = form.save(commit=False)
                payment.Payment_User=request.user
                payment.Vaccine=Vaccine.objects.get(id=id)
                payment.Total_amount=total
                form.save()
                return redirect('vaccine:registration_successfully')
            else:
                print(form.errors)
                return render(request, 'vaccine/payment.html', dict)

    except Exception as e:
        return render(request, 'vaccine/payment.html', dict)

    return render(request, 'vaccine/payment.html', dict)

def vaccine_edit(request,id):
    vaccine = Vaccine.objects.get(Vaccine_Id=id)
    form = VaccineForm(request.POST or None, request.FILES or None, instance=vaccine)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('vaccine:vaccine_list_view')
    return render(request,'vaccine/vaccine_edit.html',{'form':form})