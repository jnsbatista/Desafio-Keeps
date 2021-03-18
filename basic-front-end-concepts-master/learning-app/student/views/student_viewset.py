# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from student.models import Student
from student.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def __init__(self):
        pass

    def get_queryset(self):
        return Student.objects.filter()

    def get_serializer_class(self):
        return StudentSerializer
