from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json
from django.http import HttpResponse

# Create your views here.
class EmployeeDetailCBV(View):

    def get(self,request,*args,**kwargs):
        emp=Employee.objects.get(id=1)
        emp_data={
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr
        }
        json_data=json.dumps(emp_data)
        return HttpResponse(json_data,content_type='application/json')




from django.shortcuts import render

# Create your views here.
