from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('convert_hdr_to_png/', views.convert_hdr_to_png, name='convert_hdr_to_png')
]

