# Generated by Django 4.0.5 on 2023-01-31 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_students_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='classname',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]