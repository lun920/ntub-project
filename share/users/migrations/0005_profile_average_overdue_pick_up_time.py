# Generated by Django 4.2.11 on 2024-05-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_review_review_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="average_overdue_pick_up_time",
            field=models.IntegerField(default=0),
        ),
    ]