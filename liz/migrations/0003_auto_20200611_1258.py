# Generated by Django 3.0.7 on 2020-06-11 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liz', '0002_employee_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='depaptment',
            new_name='department',
        ),
    ]