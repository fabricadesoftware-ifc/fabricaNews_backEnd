from django.db import models


class Feeling(models.Model):
    description = models.CharField(max_length=50, null=False, blank=False)
    emoji = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return f"{self.description}"
