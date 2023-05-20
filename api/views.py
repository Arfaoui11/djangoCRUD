from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from api.models import Student

from .serializers import StudentSerializer


@api_view(['GET'])
def index(request):
    student = Student.objects.all()
    serialStudents = StudentSerializer(student, many=True)
    return Response(serialStudents.data)


@api_view(['GET'])
def studentView(request, pk):
    student = Student.objects.get(id=pk)
    serialStudent = StudentSerializer(student, many=False)
    return Response(serialStudent.data)


@api_view(['POST'])
def addStudent(request):
    serialdata = StudentSerializer(data=request.data)
    if serialdata.is_valid():
        serialdata.save()

    return Response(serialdata.data)

@api_view(['PUT'])
def studentUpdate(request, pk):
    student = Student.objects.get(id=pk)
    serialdata = StudentSerializer(instance=student, data=request.data)
    if serialdata.is_valid():
        serialdata.save()

    return Response(serialdata.data)

@api_view(['DELETE'])
def studentDelete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    students = Student.objects.all()
    serialStudents = StudentSerializer(students, many=True)
    return Response(serialStudents.data)
