from django.db import models
from django.utils import timezone

class SiteNews(models.Model):
    title = models.CharField("Title of news", max_length=25)
    text = models.CharField("Not full text of news", max_length=120)
    date = models.DateField("Date of publish", default=timezone.now)
    icon = models.CharField("Classes of icon", default="fa-solid fa-cubes", blank=True)
