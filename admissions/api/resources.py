from tastypie.resources import ModelResource, Resource
from admissions.models import Student, AdmissionRequest
from django.db.models import Count

class StudentResource(ModelResource):
    class Meta:
        queryset = Student.objects.all()
        allowed_methods = ['get']

class AdmissionRequestResource(ModelResource):
    class Meta:
        queryset = AdmissionRequest.objects.all()
        allowed_methods = ['get']

class AdmissionsByDate(Resource):
    class Meta:
        resource_name = "foobar"
        queryset = AdmissionRequest.objects.values('date').annotate(count=Count('date'))
        allowed_methods = ['get']
