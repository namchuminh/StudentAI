# Generated by Django 4.0.5 on 2023-01-21 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_students_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]