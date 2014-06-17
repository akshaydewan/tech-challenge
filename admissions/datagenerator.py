from models import Student, AdmissionRequest
from datetime import date, timedelta
from decimal import Decimal
import random

NAMES = (
    'A',
    'B',
    'C',
    'D',
)

GENDERS = (
    'M',
    'F',
)

AGES = ( 18, 19, 20, 21, 22, 23, 24 )

DEPARTMENTS = (
    'D1',
    'D2',
    'D3',
    'D4',
)

UNIVERSITIES = (
    'U1',
    'U2',
    'U3',
    'U4',
)

STATUS = (
    'PENDING',
    'APPROVED',
    'REJECTED',
)

DATE_RANGE = []
for i in range(-4,4):
    DATE_RANGE.append(date.today() + timedelta(days = i))

def generate(count=100):
    records = []
    for n in range(count):
        student = generateStudent()
        admissionRequest = generateAdmissionRequest()
        records.append((student, admissionRequest))
    return records

def generateStudent():
    student = Student()
    student.name = random.choice(NAMES)
    student.gender = random.choice(GENDERS)
    student.age = random.choice(AGES)
    student.university = random.choice(UNIVERSITIES)
    student.department = random.choice(DEPARTMENTS)
    student.percent_sem1 = randomPercent()
    student.percent_sem2 = randomPercent()
    student.percent_sem3 = randomPercent()
    student.percent_sem4 = randomPercent()
    return student

def generateAdmissionRequest():
    request = AdmissionRequest()
    request.date = random.choice(DATE_RANGE)
    request.department = random.choice(DEPARTMENTS)
    request.status = random.choice(STATUS)
    return request


def randomPercent():
    return Decimal(str(random.randrange(35, 99)) + '.' + str(random.randrange(0, 99)))

