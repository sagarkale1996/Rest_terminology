from django.urls import path,include
from .import views
from .views import EmployeeDetailCBV

urlpatterns=[
    path('api/',views.EmployeeDetailCBV.as_view())
]