# Generated by Django 4.1 on 2022-10-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_place_prder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mktorder',
            name='invoice',
            field=models.CharField(blank=True, db_index=True, max_length=15, null=True, unique=True),
        ),
    ]