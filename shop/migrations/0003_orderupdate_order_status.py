# Generated by Django 5.2.3 on 2025-07-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_orderupdate_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderupdate',
            name='order_status',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
