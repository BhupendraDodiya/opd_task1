from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.doctor_dashboard,name='dashboard'),
    path('patient/',views.patient_dashboard,name='patient'),
    path('doctor_data/<str:name>/',views.doctor_data,name='doc_data'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)