# Generated by Django 4.2 on 2023-04-17 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_userinteractions"),
    ]

    operations = [
        migrations.CreateModel(
            name="Favorites",
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
                    "news_id",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="core.news"),
                ),
                (
                    "user_id",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="core.user"),
                ),
            ],
        ),
    ]
