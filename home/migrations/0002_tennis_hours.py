# Generated by Django 5.0.5 on 2024-11-08 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tennis",
            name="hours",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
