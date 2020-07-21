from rest_framework import serializers
from .models import * 


class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResponsable
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class ServiceSignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSignature
        fields = '__all__'


class ServiceClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceClass
        fields = '__all__'

