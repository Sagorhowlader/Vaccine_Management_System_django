from django.db import models
from django.contrib.auth.models import User

BLOOD_CHOICE = {
    ('A+', 'A+'),
    ('O+', 'O+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('A-', 'A-'),
    ('O-', 'O-'),
    ('B-', 'B-'),
    ('AB-', 'AB-'),
}
Gender_Chose = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    second_name = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=10, choices=Gender_Chose, blank=True)
    mobile = models.IntegerField(default=0, blank=True)
    blood = models.CharField(max_length=10, choices=BLOOD_CHOICE, blank=True)
    NID = models.IntegerField(default=0, blank=True)
    image = models.ImageField(upload_to='profile/', blank=True)

    def get_question(self):
        return self.question_set.all()


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

    def get_answer(self):
        return self.answer_set.all()


CHOICE = {
    ('Yes', 'yes'),
    ('No', 'no')
}


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=10, choices=CHOICE)


class Feddback(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Email = models.EmailField()
    Body = models.CharField(max_length=255,blank=False)
    Subject = models.CharField(max_length=255,blank=True)
    create = models.DateTimeField(auto_now_add=True)


