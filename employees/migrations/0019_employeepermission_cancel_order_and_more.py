# Generated by Django 4.1.2 on 2022-11-02 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0018_rename_edit_employeepermission_edit_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeepermission',
            name='cancel_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeepermission',
            name='confirm_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeepermission',
            name='exchange_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeepermission',
            name='return_order',
            field=models.BooleanField(default=False),
        ),
    ]