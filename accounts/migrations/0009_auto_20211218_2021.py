# Generated by Django 3.2.9 on 2021-12-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_menuelement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='district',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
