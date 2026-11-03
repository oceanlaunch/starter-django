from django.db import models


class Visit(models.Model):
    """One row per visit to the home page: shows the database is connected and keeps data across deploys."""

    at = models.DateTimeField(auto_now_add=True)
