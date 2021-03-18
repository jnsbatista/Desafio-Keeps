# -*- coding: utf-8 -*-
from rest_framework import serializers
from enrollment.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = '__all__'
        depth = 2


class EnrollmentSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Enrollment
        fields = '__all__'
