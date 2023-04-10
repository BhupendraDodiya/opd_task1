from django.db import models

# Create your models here.
category_choices = (
    ('Lungs','Lungs'),
    ('Heart','Heart'),
    ('Eyes','Eyes'),
    ('Legs','Legs'),
    ('Ears','Ears'),
)

experience_choices = (
    ('10 years','10 years'),
    ('20 years','20 years'),
    ('30 years','30 years'),
    ('35 years','35 years'),
    ('40 years','40 years'),
    
)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,choices=category_choices)
    image = models.ImageField(upload_to='doctor_image/',)
    experience = models.CharField(max_length=100,choices=experience_choices)
    appointment = models.DateTimeField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    issue = models.CharField(max_length=100,choices=category_choices)
    select_doctor = models.ForeignKey(Doctor ,on_delete=models.CASCADE)
    appointment = models.DateTimeField()
   