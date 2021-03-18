# -*- coding: utf-8 -*-

from rest_framework import serializers
from course.models.course import Course, CourseCategory


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCategory
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = '__all__'
