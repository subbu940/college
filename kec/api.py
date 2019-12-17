from rest_framework.views import APIView
from .serializers import StudentApplicationSerializer, DepartmetntSerializer, StaffSerializer
from .models import StudentApplication, Department, Staff
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class AppView(APIView):
    def get(self, request, format=None):
        users = StudentApplication.objects.all()
        serializer = StudentApplicationSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentView(APIView):
    def get(self, request, format=True):
        user = Department.objects.all()
        serializer = DepartmetntSerializer(user, many=True)
        return Response(serializer.data)


class StaffView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        users = Staff.objects.all()
        serializer = StaffSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
