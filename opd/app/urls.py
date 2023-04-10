from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('doctor/',views.doctor_dashboard,name='doctor'),
    path('patient/',views.patient_dashboard,name='patient'),
    path('doctor_data/<str:name>/',views.doctor_data,name='doc_data'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)