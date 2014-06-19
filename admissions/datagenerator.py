from models import Student, AdmissionRequest
from datetime import date, timedelta
from decimal import Decimal
import random

GENDERS = (
    'M',
    'F',
)

AGES = ( 18, 19, 20, 21, 22, 23, 24 )

DEPARTMENTS = (
    'COMPUTER_SCIENCE',
    'MICROBIOLOGY',
    'AERONAUTICS',
    'MEDICINE',
)

UNIVERSITIES = (
    'MUMBAI',
    'DELHI',
    'PUNE',
    'CHENNAI',
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


NAMES = (
'Melinda Dickens',
'Lekisha Redinger',
'Graciela Decelles',
'Dane Hodgdon',
'Rex Hendren',
'Sarina Welton',
'Barbra Zuchowski',
'Stacie Wittner',
'Pasty Mcdill',
'Tora Wacker',
'Ruthe Spofford',
'Hollie Crowther',
'Fabian Castiglione',
'Marylee Lozier',
'Danyell Mcphillips',
'Omar Archey',
'Karima Kramer',
'Mitchel Beazley',
'Marilu Mansell',
'Robbie Hessler',
'Clare Wingler',
'Kassandra Olea',
'Adaline Patman',
'Josephina Schwab',
'Carrie Eaker',
'Jannet Sobieski',
'Ward Topps',
'Hanh Hilliker',
'Maryellen Saeger',
'Tonia Hodder',
'Kaitlin Ransdell',
'Delena Bak',
'Betsy Biles',
'Earnest Souza',
'Birdie Vaillancourt',
'Rebecca Gaughan',
'Randee Crupi',
'Carolyn Shephard',
'Rosendo Sanders',
'Jung Alvis',
'Alonso Burkhalter',
'Elvera Stodola',
'Kitty Praylow',
'Bunny Mitchum',
'Trudie Sentell',
'Tamesha Manrique',
'Eleni Guinyard',
'Vella Rost',
'Wilda Trueblood',
'Chauncey Pastrana',
'Shan Weatherspoon',
'Cheryll Sola',
'Kenton Faught',
'Zulema Malone',
'Chong Helsley',
'Deangelo Pavelka',
'Indira Hamburg',
'Lorinda Shivers',
'Evelina Rothrock',
'Lorilee Bonneau',
'Edwina Caro',
'Shane Dunn',
'Gino Zahradnik',
'Verlene Annunziata',
'Myong True',
'Isobel Eldredge',
'Florentino Leandro',
'Quintin Bachus',
'Constance Narron',
'Julian Ream',
'Maia Pershall',
'Elayne Filkins',
'Hugo Milton',
'Leo Parr',
'Shirely Nakamura',
'Lannie Guiterrez',
'Abbey Edison',
'Elroy Barbosa',
'Sheri Rolan',
'Eldon Curnutt',
'Clarita Madry',
'Carl Colston',
'Marilu Reny',
'Yasmin Cimmino',
'Vivien Kos',
'Jimmy Grieve',
'Francisco Varner',
'Araceli Means',
'Cory Gholston',
'Tennie Dantin',
'Calista Waterbury',
'Sang Gayer',
'Gustavo Aberle',
'Karri Lentine',
'Cesar Fretwell',
'Deann Pfannenstiel',
'Kelli La',
'Heather Bak',
'Petra Elliston',
'Esther Wamsley',
)
