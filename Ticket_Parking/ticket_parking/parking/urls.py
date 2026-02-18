
from django.urls import path
from . import views

urlpatterns = [
    path('parking/',views.home,name='home'),
    path('enter/',views.enter_vehicle,name='enter_vehicle'),
    path('bill/',views.generate_bill,name='generate_bill'),
]    