# Generated by Django 3.2.9 on 2021-12-18 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mail',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
