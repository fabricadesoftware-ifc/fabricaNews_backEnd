# Generated by Django 4.2 on 2023-04-17 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInteractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_type', models.CharField(max_length=20)),
                ('interaction_time', models.DateTimeField(auto_now_add=True)),
                ('has_notification', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserInteractions', to='core.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserInteractions', to='core.user')),
            ],
        ),
    ]
