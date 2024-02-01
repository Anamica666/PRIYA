from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from student_application.models import StudentInfo

class SaveStudentInfo(APIView):
    def post(self, request):
        data = request.data
        name = data.get('name')
        age = data.get('age')
        student_class = data.get('Student_class')

        try:
            student_obj = StudentInfo(name=name, age=age, student_class=student_class)
            student_obj.save()
            return Response({
                'status': 'success',
                'message': 'Data saved successfully.',
                'status_code': status.HTTP_200_OK
            })
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e),
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR
            })
