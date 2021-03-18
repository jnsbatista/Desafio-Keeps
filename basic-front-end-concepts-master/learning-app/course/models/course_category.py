# -*- coding: utf-8 -*-
import uuid
from django.db import models


class CourseCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=200)
    description = models.TextField(verbose_name="Description", null=True, blank=True)

    class Meta:
        app_label = 'course'
        verbose_name_plural = "Course Category"
        db_table = 'course_category'


