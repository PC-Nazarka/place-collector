# Generated by Django 3.2.13 on 2022-05-24 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("collector", "0005_auto_20220525_0307"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="latitude",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="place",
            name="longitude",
            field=models.FloatField(),
        ),
    ]
