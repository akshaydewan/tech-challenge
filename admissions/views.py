from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'admissions/index.html')

def generateData(request):
    return render(request, 'admissions/generate.html')

