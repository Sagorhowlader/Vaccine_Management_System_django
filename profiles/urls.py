from django.urls import path, include
from django.contrib.auth import views as auth_view
from .views import *
from bd_vaccine.views import pendingpatient,completedpatient
app_name='patient'
urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('patient-dashboard',patient_dashboard_view,name='patient-dashboard'),
    path('afterlogin', afterlogin_view, name='afterlogin'),
    path('signup/', SignUp.as_view(), name='singup'),
    path('makeappointment/',makeappointment,name='makeappointment'),
    path('create-profile/',Create_Profile,name='create_profile'),
    path('create_schedule/',create_schedule,name='create_schedule'),
    path('pendingpatient/',pendingpatient,name='pendingpatient'),
    path('completedpatient/',completedpatient,name='completedpatient'),
    path('patient_list_view/',ListViewPatient.as_view(),name='patient_list_view'),
    path('patient_deleted/<int:id>',patient_delete,name='patient_deleted'),
    path('payment_report/',payment_report,name='patient_report'),
    path('vaccine_report/<int:pk>',vaccine_report,name='vaccine_report'),
    path('vaccination_edit/<int:id>', edit_vaccine, name='vaccination_edit'),
    path('vaccination_deleted/<int:id>', deleted_vaccine, name='vaccination_deleted'),
    path('feedback/', feedback, name='feedback'),


]