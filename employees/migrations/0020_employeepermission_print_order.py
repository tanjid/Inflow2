# Generated by Django 4.1.2 on 2022-11-02 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0019_employeepermission_cancel_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeepermission',
            name='print_order',
            field=models.BooleanField(default=False),
        ),
    ]
