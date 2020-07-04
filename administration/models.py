from django.db import models


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
    bank_account_number = models.CharField(max_length=50, unique=True)


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


class Signature(models.Model):
    LEVEL_CHOICE = [
        ('B', 'Bachiller'),
        ('S', 'University'),        
    ]

    name = models.CharField(max_length=20)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICE)


class Teacher(Person):
    signature = models.ManyToManyField(Signature, related_name='signatures')





