# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from course.models import CourseCategory
from course.serializers import CourseCategorySerializer


class CourseCategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_queryset(self):
        return CourseCategory.objects.filter()

    @staticmethod
    def get_serializer_class():
        return CourseCategorySerializer
