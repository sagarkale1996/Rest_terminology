from django.urls import path
from  .import views
from .views import JsonCBV

urlpatterns=[
    path('j/', views.emp_view),
    path('json/', views.emp_json_data),
    path('jcv/',JsonCBV.as_view())

]
