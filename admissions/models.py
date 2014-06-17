from django.db import models

class Student(models.Model):
        GENDERS = (
                ('M', 'Male'),
                ('F', 'Female')
        )
	name = models.CharField(max_length=200)
        gender = models.CharField(max_length=1, choices=GENDERS)
        age = models.IntegerField()
        university = models.CharField(max_length=200)
        department = models.CharField(max_length=200)
        percent_sem1 = models.DecimalField(max_digits=4, decimal_places=2)
        percent_sem2 = models.DecimalField(max_digits=4, decimal_places=2)
        percent_sem3 = models.DecimalField(max_digits=4, decimal_places=2)
        percent_sem4 = models.DecimalField(max_digits=4, decimal_places=2)
        
        def __unicode__(self):
                return self.name
        
class AdmissionRequest(models.Model):
        STATUS = (
                ('PENDING', 'Pending'),
                ('APPROVED', 'Approved'),
                ('REJECTED', 'Rejected')
        )
        student = models.ForeignKey(Student)
        date = models.DateField()
        department = models.CharField(max_length=200)
        status = models.CharField(max_length=40)
        #processed_by = models.CharField(max_length=200)
        
        def __unicode__(self):
                return self.student.name
