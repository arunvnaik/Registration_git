from django.urls import path 
from .views import RegistrationList,RegistrationDetail 

urlpatterns = [
    path('registrations/', RegistrationList.as_view(), name ='registration-list'),
    path('registrations/<int:pk>/', RegistrationDetail.as_view(), name='registration-detail'),
]
