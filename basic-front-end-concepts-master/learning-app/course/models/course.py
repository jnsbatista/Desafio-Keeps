# -*- coding: utf-8 -*-

import uuid
from django.db import models
from course.models.course_category import CourseCategory


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=200)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    category = models.ForeignKey(CourseCategory, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    class Meta:
        app_label = 'course'
        verbose_name_plural = "Courses"
        db_table = 'course'
