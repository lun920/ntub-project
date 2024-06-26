# Generated by Django 4.2.10 on 2024-04-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0005_order_request_time_alter_order_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='breakage',
            field=models.IntegerField(choices=[(0, '0'), (10, '10'), (20, '20'), (30, '30'), (40, '40'), (50, '50'), (60, '60'), (70, '70'), (80, '80'), (90, '90'), (100, '100')], default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('wait_to_pay', 'Wait To Pay'), ('pending', 'Pending'), ('unpaid', 'Unpaid'), ('accept', 'Accept'), ('deny', 'Deny'), ('cancel_order', 'Cancel Order'), ('get_item', 'Get Item'), ('return_item', 'Return Item'), ('borrower_comment ', 'Borrower Comment'), ('finish', 'Finish')], max_length=20),
        ),
    ]
