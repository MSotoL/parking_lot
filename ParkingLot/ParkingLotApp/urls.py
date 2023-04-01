from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),    
    path('guardar_plaza_BD', views.guardarPlazaBD, name="guardarPlazaBD"),
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)