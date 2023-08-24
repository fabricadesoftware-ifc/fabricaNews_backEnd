from django.db import models

from project.models.project import Project
from user.models import User

from .category import Category


class News(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="News"
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    text = models.CharField(max_length=5000, null=False, blank=False)
    date_pub = models.DateField(null=False, blank=False)
    user_pub = models.ForeignKey(User, on_delete=models.PROTECT, related_name="News")
    public = models.BooleanField(null=False, blank=False)
    tags = models.JSONField(null=False, blank=False)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name="News")
    revision_date = models.DateTimeField(null=False, blank=False)
    status = models.CharField(max_length=20, null=False, blank=False)
    needs_revision = models.BooleanField(null=False, blank=False)
    needs_approval = models.BooleanField(null=False, blank=False)
    relevance = models.IntegerField(null=False, blank=False)
    accuracy = models.IntegerField(null=False, blank=False)
    update_date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return f"{self.title}"
