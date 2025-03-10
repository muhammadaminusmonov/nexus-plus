from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    sorting = models.SmallIntegerField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
