# Generated by Django 5.0.1 on 2024-01-30 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_application', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='StudentInfo',
        ),
    ]