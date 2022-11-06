# Generated by Django 4.1.2 on 2022-11-06 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0006_alter_neworder_mobille_number_alter_neworder_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('details', models.CharField(max_length=250)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='orders.neworder')),
            ],
        ),
    ]