# Generated by Django 4.2 on 2023-04-17 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_comments_newsfeel_delete_news"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=200)),
                ("text", models.CharField(max_length=5000)),
                ("date_pub", models.DateField()),
                ("public", models.BooleanField()),
                ("tags", models.JSONField()),
                ("revision_date", models.DateTimeField()),
                ("status", models.CharField(max_length=20)),
                ("needs_revision", models.BooleanField()),
                ("needs_approval", models.BooleanField()),
                ("relevance", models.IntegerField()),
                ("accuracy", models.IntegerField()),
                ("update_date", models.DateTimeField()),
                (
                    "category_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="News",
                        to="core.category",
                    ),
                ),
                (
                    "user_pub_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="News",
                        to="core.user",
                    ),
                ),
            ],
        ),
    ]
