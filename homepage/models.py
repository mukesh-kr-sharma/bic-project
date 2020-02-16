from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CandidateDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField("Phone number", max_length=10)
    gender = models.CharField("Gender", max_length=50, choices=(('M', 'Male'), ('F', 'Female')))
    dob = models.DateField("Date of birth", auto_now=False, auto_now_add=False)
    address = models.TextField("Address")
    aadhar_no = models.IntegerField("Aadhar Number")
    aadhar_pic = models.ImageField("Aadhar image",
        upload_to="%y/%m/%d",
        height_field=None,
        width_field=None,
        max_length=None
    )

    def __str__(self):
        return self.user.username + " (" + self.user.first_name + " " + self.user.last_name + ")"
    