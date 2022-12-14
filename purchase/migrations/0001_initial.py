# Generated by Django 4.1 on 2022-10-16 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('sell_price', models.IntegerField(blank=True, null=True)),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('purchase_note', models.CharField(blank=True, max_length=15, null=True)),
                ('grand_total', models.IntegerField(blank=True, null=True)),
                ('items', models.ManyToManyField(blank=True, to='purchase.purchaseitems')),
            ],
        ),
    ]
