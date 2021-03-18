# -*- coding: utf-8 -*-
import uuid
from django.db import models


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=200)
    email = models.EmailField(verbose_name="Email", max_length=200, null=True, blank=True)
    status = models.BooleanField(verbose_name="Status", default=True)
    phone = models.CharField(verbose_name="Phone", max_length=20, null=True, blank=True)

    last_access_date = models.DateTimeField(verbose_name="Last Access Date", null=True, blank=True)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    class Meta:
        app_label = 'student'
        verbose_name_plural = "Students"
        db_table = 'student'
