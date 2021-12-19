# Generated by Django 3.2.9 on 2021-12-19 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_order_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='done',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='done',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Restaurant Approved', 'Restaurant Approved'), ('Restaurant Declined', 'Restaurant Declined')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Restaurant Approved', 'Restaurant Approved'), ('Restaurant Declined', 'Restaurant Declined')], max_length=100, null=True),
        ),
    ]
