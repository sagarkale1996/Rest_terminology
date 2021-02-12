from django.shortcuts import render,HttpResponse

# Create your views here.

def emp_view(request):
    emp={
        'eName':"sagar",
        'eage':23,
        'esal':25000
    }
    res="EMPname:{}<br>Eage:{}<br>Esal:{}".format(emp['eName'],emp['eage'],emp['esal'])
    return HttpResponse(res)

import json
from django.http import JsonResponse
def emp_json_data(request):
    emp = {
        'eName': "sagar",
        'eage': 23,
        'esal': 25000
    }
    #return JsonResponse(emp)
    json_data=json.dumps(emp)
    return HttpResponse(json_data)

from django.views.generic import View

class JsonCBV(View):

    def get(self,request,*args,**kwargs):
        emp = {
            'eName': "sagar",
            'eage': 23,
            'esal': 25000
        }

        jason_data=json.dumps({"msg":"this is json Data"})
        return HttpResponse(jason_data)

