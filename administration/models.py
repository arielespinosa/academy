

from django.db import models
from datetime import date


class Signature(models.Model):
    LEVEL_CHOICE = [
        ('B', 'Bachiller'),
        ('S', 'University'),        
    ]

    name = models.CharField(max_length=20)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICE)

    def __str__(self):
        return self.name


class Phone(models.Model):
    DESCRIPTION_CHOICE = [
        ('H', 'Home'),
        ('W', 'Work'),
        ('P', 'Private'),
    ]
    
    number = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=10, choices=DESCRIPTION_CHOICE, blank=True, null=True)
    
    def __str__(self):
        return self.number


class Email(models.Model):
    DESCRIPTION_CHOICE = [
        ('H', 'Home'),
        ('W', 'Work'),
        ('P', 'Private'),
    ]
    
    email = models.EmailField(blank=True, null=True)
    description = models.CharField(max_length=10, choices=DESCRIPTION_CHOICE, blank=True, null=True)

    def __str__(self):
        return self.email


class Person(models.Model):
    dni = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.ManyToManyField(Phone, related_name='phones')
    email = models.ManyToManyField(Email, related_name='emails')

    def __str__(self):
        return self.name


class Responsable(Person):
    bank_account = models.CharField(max_length=50, unique=True)


class Student(Person):
    LEVEL_CHOICE = [
        ('B', 'Bachiller'),
        ('S', 'University'),        
    ]

    scholar_level = models.CharField(max_length=20, choices=LEVEL_CHOICE)
    responsables = models.ManyToManyField(Responsable, related_name='responsables')


class StudentResponsable(models.Model):
    RELATIONSHIP_CHOICE = [
        ('F', 'Father'),
        ('M', 'Mother'),
        ('T', 'Tutor'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=10, choices=RELATIONSHIP_CHOICE, blank=True, null=True)


class Teacher(Person):
    aviable_signature = models.ManyToManyField(Signature, related_name='signatures')
    bank_account = models.CharField(max_length=50, unique=True)


class ServicePlace(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    name = models.CharField(max_length=150)
  
    def __str__(self):
        return self.name


class ServiceSignature(models.Model):
    TIME_SECCTION_CHOICE = [
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Nigth'),
    ]

    code = models.CharField(max_length=10)
    place = models.ForeignKey(ServicePlace, related_name='service_places', on_delete=models.CASCADE)
    typeof = models.ForeignKey(ServiceType, related_name='service_type', on_delete=models.CASCADE)
    time_section = models.CharField(max_length=20, choices=TIME_SECCTION_CHOICE)
    cost = models.FloatField()
    salary = models.FloatField()

    def __str__(self):
        return self.code


class ServiceClass(models.Model):
    contract = models.CharField(max_length=10)
    start_date = models.DateField()
    finish_date = models.DateField()
    hours = models.FloatField() # Diarias o totales?
    service = models.ForeignKey(ServiceSignature, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='students', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='teachers', on_delete=models.CASCADE)
    facture = models.CharField(max_length=50)

    def __str__(self):
        return self.contract

    def on_course(self):
        date_now = date.today()
        return self.start_date < date_now < self.finish_date

    

