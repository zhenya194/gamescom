from django.db import models
from django.utils import timezone

class GamesNews(models.Model):
    title = models.CharField("Title of article", max_length=25)
    image = models.ImageField(
        "Upload an image of this artcile",
        upload_to="articles/")
    text = models.TextField("Full text of article")
    date = models.DateField("Date of publish", default=timezone.now)
