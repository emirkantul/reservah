# Generated by Django 3.2.9 on 2021-12-19 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_order_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cost',
        ),
    ]
