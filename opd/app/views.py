from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    doc = Doctor.objects.all()
    pat = Patient.objects.all()
    return render(request,'home.html',{'doc':doc,'pat':pat})

def doctor_dashboard(request):
    doc = Doctor.objects.all()
    return render(request,'Dashboard.html',{'doc':doc})

def patient_dashboard(request):
    pat = Patient.objects.all()
    return render(request,'Patient.html',{'pat':pat})

def doctor_data(request,name):
    doc = Doctor.objects.filter(name=name)
    return render(request,'doctor_data.html',{'doc':doc})

