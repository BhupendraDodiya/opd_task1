from django.contrib import admin
from app.models import Doctor,Patient
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','name','category','experience','appointment']

@admin.register(Patient)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','name','contact','email','address','issue','select_doctor']