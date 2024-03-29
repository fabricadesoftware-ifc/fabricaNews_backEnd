# Generated by Django 4.2.2 on 2023-06-29 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0016_remove_project_user"),
        ("user", "0002_alter_userinteractions_project_and_more"),
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="News",
                to="project.project",
            ),
        ),
        migrations.DeleteModel(
            name="Project",
        ),
    ]
