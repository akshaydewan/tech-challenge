from django.shortcuts import render
from django.http import HttpResponse
from models import AdmissionRequest, Student
import datagenerator

# Create your views here.
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

