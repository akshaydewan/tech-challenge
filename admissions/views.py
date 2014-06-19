from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from models import AdmissionRequest, Student
import datagenerator
from django.db.models import Count
from django.core import serializers
from django.utils import simplejson


def index(request):
    return render(request, 'admissions/index.html')

def generateData(request):
    if request.POST:
        list = datagenerator.generate()
        AdmissionRequest.objects.all().delete()
        Student.objects.all().delete()
        for record in list:
            student = record[0]
            admissionRequest = record[1]
            student.save()
            admissionRequest.student = student
            admissionRequest.save()
        return HttpResponse('')
    else:
        return render(request, 'admissions/generate.html')

def handleRestRequest(request):
    allowedGroupBy = ['age', 'gender', 'date', '']
    groupBy = request.GET.get("groupBy", "")
    genderFilter = request.GET.getlist("gender")
    departmentFilter = request.GET.getlist("department")
    universityFilter = request.GET.getlist("university")
    if groupBy not in allowedGroupBy:
        return HttpResponseBadRequest('allowed grouping: ' + ' '.join(allowedGroupBy))
    if groupBy == 'date':
        #values = AdmissionRequest.objects.values('date').annotate(count=Count('date'))
        values = getAdmissionCount(genderFilter, departmentFilter, universityFilter)
        response = simplejson.dumps(createDict(values))
        return HttpResponse(response, content_type='application/json')
    else:        
        response = serializers.serialize("json", AdmissionRequest.objects.all())
        return HttpResponse(response)

def getAdmissionCount(genderFilter, departmentFilter, universityFilter):
    q = AdmissionRequest.objects.all()
    if genderFilter:
        q = q.filter(student__gender__in=genderFilter)
    if departmentFilter:
        q = q.filter(department__in=departmentFilter)
    if universityFilter:
        q = q.filter(student__university__in=universityFilter)
    return q.values('date').annotate(count=Count('date'))
        

def createDict(values):
    list = []
    for value in values:
        date = str(value.get('date'))
        count = value.get('count')
        list.append({'date' : date, 'count': count})
    return list
