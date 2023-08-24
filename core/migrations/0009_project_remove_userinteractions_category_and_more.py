# Generated by Django 4.2 on 2023-04-24 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_favorites"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="projects",
                        to="core.user",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="userinteractions",
            name="category",
        ),
        migrations.AddField(
            model_name="comments",
            name="news",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="comments",
                to="core.news",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="newsfeel",
            name="news",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="news_feels",
                to="core.news",
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="UserProjectFollow",
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
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_project_follows",
                        to="core.project",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_project_follows",
                        to="core.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Save_to_read",
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
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="save_to_reads",
                        to="core.news",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="save_to_reads",
                        to="core.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="news",
            name="project_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="News",
                to="core.project",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userinteractions",
            name="project",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="UserInteractions",
                to="core.project",
            ),
            preserve_default=False,
        ),
    ]
