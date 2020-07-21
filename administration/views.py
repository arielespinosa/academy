from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *


class ResponsableViewSet(viewsets.ModelViewSet):
    serializer_class = ResponsableSerializer
    queryset = Responsable.objects.all()


class ResponsableListView(generics.ListAPIView):
    serializer_class = ResponsableSerializer
    queryset = Responsable.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentResponsableViewSet(viewsets.ModelViewSet):
    serializer_class = StudentResponsableSerializer
    queryset = StudentResponsable.objects.all()


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class ServiceSignatureViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSignatureSerializer
    queryset = ServiceSignature.objects.all()


class ServiceClassViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceClassSerializer
    queryset = ServiceClass.objects.all()


