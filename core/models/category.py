from django.db import models


class Category(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description