# Generated by Django 4.0.5 on 2023-02-08 10:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0004_classname_slug'),
        ('subjects', '0004_subject_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('classname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.classname')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.students')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject')),
            ],
        ),
    ]
