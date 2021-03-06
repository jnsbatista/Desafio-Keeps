# Generated by Django 2.2 on 2021-03-03 19:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.Student', verbose_name='Student')),
            ],
            options={
                'verbose_name_plural': 'Enrollments',
                'db_table': 'enrollment',
            },
        ),
    ]
