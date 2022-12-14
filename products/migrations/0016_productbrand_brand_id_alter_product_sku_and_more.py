# Generated by Django 4.1.2 on 2022-11-05 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_warranty'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='brand_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(db_index=True, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='warranty',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
    ]
