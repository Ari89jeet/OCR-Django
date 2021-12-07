
from request.models import PricingRequest
from .models import PricingRequest, myuploadfile, myuploadfile_excel
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseRedirect
from django.views.generic.base import View
from .resources import PricingRequest, PricingRequestResource
import pandas as pd
from django import forms
import django_excel as excel
from tablib import Dataset
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from openpyxl import Workbook


import xlwt
# Create your views here.


""" def index(request):
    context = {
        "data": myuploadfile.objects.all(),
    }
    return render(request, "upload/multiple.html", context) """


class UploadFileForm(forms.Form):
    file = forms.FileField()

# Create your views here.


def send_files(request):
    
    if "button1" in request.POST:
        myuploadfile.objects.all().delete()
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")

        for f in myfile:
            myuploadfile(f_name=name, myfiles=f).save()

        return render(request, 'request/input.html')
    
    if "button3" in request.POST:
        myuploadfile_excel.objects.all().delete()
        myfile = request.FILES['myfile1']

        myuploadfile_excel(myfiles=myfile).save()

        return render(request, 'request/input.html')

    if "button2" in request.POST:
        PricingRequest.objects.all().delete()
        PricingRequest_Resource = PricingRequestResource()
        dataset = Dataset()
        new_request = request.FILES['myfile']   
        
        
        imported_data = dataset.load(new_request.read(), format='xlsx')
        print(imported_data)
        
        for data in imported_data:
            PricingRequest.objects.create(
               PartNumber = data[0],
               Nomenclature=data[1],
               Quantity = data[2]             
               
            )
        
            #print(data)
        return render(request, 'request/input.html')
    
    return render(request, 'request/input.html')

        
    

def hello_world(request):
    
    context={
        'Hello_World': 'hello_world'
    }
    return render(request, 'request/input_copy.html', context)
 
