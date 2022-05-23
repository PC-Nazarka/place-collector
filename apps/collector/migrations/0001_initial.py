# Generated by Django 3.2.13 on 2022-05-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="latitude_place"
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="longitude_place"
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="name_place")),
                ("description", models.TextField(verbose_name="description_place")),
            ],
            options={
                "verbose_name": "Place",
                "verbose_name_plural": "Places",
            },
        ),
    ]
