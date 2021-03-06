# Generated by Django 3.2.9 on 2021-12-11 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerfirstname', models.CharField(max_length=20)),
                ('customerlastname', models.CharField(max_length=30)),
                ('customerphone', models.CharField(max_length=10)),
                ('deliveryaddressline1', models.CharField(max_length=100)),
                ('deliveryaddressline2', models.CharField(blank=True, max_length=100)),
                ('deliverycity', models.CharField(max_length=30)),
                ('deliverystate', models.CharField(max_length=2)),
                ('deliveryzip', models.CharField(max_length=10)),
                ('cardnumber', models.CharField(max_length=16)),
                ('cardexpiration', models.DateField(blank=True, null=True)),
                ('cardcvv', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('addressline1', models.CharField(max_length=100)),
                ('addressline2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('isactive', models.BooleanField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveryapp.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveryapp.cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deliveryapp.item')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='deliveryapp.CartItem', to='deliveryapp.Item'),
        ),
    ]
