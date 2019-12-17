from .models import StudentApplication, Department, Staff
from rest_framework import serializers


class StudentApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentApplication
        fields = ["id", "student_name", "email", "ssc_percentage", "inter_percentage"]

    def create(self, validated_data):
        return StudentApplication.objects.create(**validated_data)

class DepartmetntSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ["id", "staff_name", "experience", "specialization", "mobile_no", "department"]

    def create(self, validated_data):
        return Staff.objects.create(**validated_data)