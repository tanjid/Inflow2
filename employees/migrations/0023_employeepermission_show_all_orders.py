# Generated by Django 4.1.2 on 2022-11-05 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0022_employeepermission_inven'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeepermission',
            name='show_all_orders',
            field=models.BooleanField(default=False),
        ),
    ]