# Generated by Django 3.2.9 on 2021-12-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_customer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
