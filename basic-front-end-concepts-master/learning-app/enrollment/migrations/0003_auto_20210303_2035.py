# Generated by Django 2.2 on 2021-03-03 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0002_auto_20210303_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course.Course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.Student', verbose_name='Student'),
        ),
    ]
