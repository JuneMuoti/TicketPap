# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable
from django.http import HttpResponse
from .resources import PersonResource

# Create your views here.


def home(request):
    table=Person.objects.all()
    
    return render(request,'index.html',{'table':table})

def export(request):
    person_resource=PersonResource()
    dataset=person_resource.export()
    response=HttpResponse(dataset.xls,content_type='application/vnd.ms-excel')
    response['Content-Disposition']='attachment;filename="persons.xls'
    return response
# def people(request):

#     return render(request,'raised.html',)