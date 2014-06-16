from django.contrib import admin
from admissions.models import AdmissionRequest, Student

# Register your models here.
admin.site.register(Student)
admin.site.register(AdmissionRequest)
