# Generated by Django 3.2.8 on 2021-11-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='addressline2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]