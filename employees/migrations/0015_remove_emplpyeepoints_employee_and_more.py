# Generated by Django 4.1.2 on 2022-11-01 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_remove_emplpyeepoints_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emplpyeepoints',
            name='employee',
        ),
        migrations.AddField(
            model_name='emplpyeepoints',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employee'),
        ),
    ]
