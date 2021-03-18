# -*- coding: utf-8 -*-
import uuid
from django.db import models

from course.models import Course
from student.models import Student


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, verbose_name="Student", on_delete=models.PROTECT)
    course = models.ForeignKey(Course, verbose_name="Course", on_delete=models.PROTECT)

    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    class Meta:
        app_label = 'enrollment'
        verbose_name_plural = "Enrollments"
        db_table = 'enrollment'
