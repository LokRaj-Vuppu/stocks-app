# Generated by Django 3.2.9 on 2021-12-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_details', '0002_alter_stocks_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
