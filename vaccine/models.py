from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vaccine(models.Model):
    Vaccine_Id= models.CharField(max_length=200,blank=False)
    Vaccine_name=models.CharField(max_length=200,blank=False)
    Vaccine_allow_age = models.CharField(max_length=200,blank=True)
    Vaccine_details = models.CharField(max_length=350, blank=True)
    Vaccine_price = models.CharField(max_length=200, blank=False)
    Vaccine_image= models.ImageField(upload_to='vaccine/',null=True,blank=False)
    def __str__(self):
        return self.Vaccine_name

    def vaccine_price(self,Vaccine_name):
        vaccine= Vaccine.objects.filter(Vaccine_name=Vaccine_name).values_list('Vaccine_price', flat=True)
        return vaccine[0]
    def vaccine_id(self,Vaccine_name):
        vaccine= Vaccine.objects.filter(Vaccine_name=Vaccine_name).values_list('id', flat=True)
        return vaccine[0]

class Stock(models.Model):
    vaccine = models.ForeignKey(Vaccine,on_delete = models.CASCADE)
    quantity= models.IntegerField(default=0)

    def __str__(self):
        return f"{self.vaccine} has {self.quantity} in stock"

class Vaccination(models.Model):
    Vaccine_name= models.ForeignKey(Vaccine,on_delete= models.CASCADE)
    User = models.ForeignKey(User,on_delete= models.CASCADE)
    First_schudle= models.DateTimeField(auto_now_add=False)
    Second_schdule = models.DateTimeField(auto_now_add=False)
    First_Status  = models.CharField(max_length=15,default='Pending')
    Second_Status = models.CharField(max_length=15, default='Pending')
    Approve = models.BooleanField(default=False)
    Payment_Status = models.BooleanField(default=False)
    Note = models.CharField(max_length=255,blank=True)
    Price = models.IntegerField()

class Payment(models.Model):
    Payment_User = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Vaccine = models.ForeignKey(Vaccine,on_delete=models.CASCADE)
    Card_No = models.CharField(max_length=20)
    Expiry_date = models.CharField(max_length=20)
    Cvv= models.IntegerField()
    Total_amount = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
