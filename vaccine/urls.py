from django.urls import path , include
from .views import *
app_name = 'vaccine'
urlpatterns = [
 path('vaccine-details/<int:pk>',DetailsVaccine.as_view(),name= 'vaccine_details'),
 path('vaccine_list_view/',ListViewVaccine.as_view(), name='vaccine_list_view'),
 path('search-vaccine/',vaccine_search, name='search-vaccine'),
 path('vaccine-add/',add_vaccine,name='vaccine-add'),
 path('vaccine-deleted/<str:id>',delete_vaccine,name='vaccine-deleted'),
 path('vaccine_warring/',vaccine_warring,name='vaccine_warring'),
 path('registration_successfully/',registration_successfully,name='registration_successfully'),
 path('payment/<int:id>',vaccine_payment,name='payment'),
 path('vaccine_edit/<str:id>',vaccine_edit,name='vaccine_edit')
]