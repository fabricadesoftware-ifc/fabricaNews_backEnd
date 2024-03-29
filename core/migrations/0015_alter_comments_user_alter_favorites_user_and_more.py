# Generated by Django 4.2.2 on 2023-06-22 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
        ("core", "0014_remove_userinteractions_project_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="comments",
                to="user.user",
            ),
        ),
        migrations.AlterField(
            model_name="favorites",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="user.user"),
        ),
        migrations.AlterField(
            model_name="news",
            name="user_pub",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="News",
                to="user.user",
            ),
        ),
        migrations.AlterField(
            model_name="newsfeel",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="news_feels",
                to="user.user",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="projects",
                to="user.user",
            ),
        ),
        migrations.AlterField(
            model_name="savetoread",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="SaveToReads",
                to="user.user",
            ),
        ),
        migrations.DeleteModel(
            name="User",
        ),
        migrations.DeleteModel(
            name="UserInteractions",
        ),
        migrations.DeleteModel(
            name="UserProjectFollow",
        ),
    ]
