from django.db import models

# Create your models here.

class Poll(models.Model):

    poll_name = models.CharField(max_length=200, blank=False, null=False, default=" ")
    poll_description = models.TextField(blank=False, null=False, default=" ")
    poll_options = models.TextField(blank=False, null=False, default="[]")
    poll_result = models.TextField(blank=False, null=False, default="[]")