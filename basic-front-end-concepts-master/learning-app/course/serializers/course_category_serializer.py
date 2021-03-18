# -*- coding: utf-8 -*-

from rest_framework import serializers

from course.models.course_category import CourseCategory


class CourseCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCategory
        fields = '__all__'
