# Generated by Django 4.1.2 on 2022-11-07 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_neworder_mobille_number_alter_neworder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neworder',
            name='invoice_number',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='CompleteOrderData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_status', models.CharField(max_length=50)),
                ('after_rtn_note', models.TextField(blank=True, null=True)),
                ('after_verf', models.BooleanField(default=False)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='orders.neworder')),
            ],
        ),
    ]