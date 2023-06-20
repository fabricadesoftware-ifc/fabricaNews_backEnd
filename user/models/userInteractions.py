from django.db import models
from user.models import User
from user.models import Project


class UserInteractions(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="UserInteractions"
    )
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, related_name="UserInteractions"
    )
    interaction_type = models.CharField(max_length=20, null=False, blank=False)
    interaction_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    has_notification = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f"{self.interaction_type}"
