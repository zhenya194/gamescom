from django.db import models

class SiteNews(models.Model):
    title = models.CharField("Title of news", max_length=15)
    text = models.CharField("Not full text of news", max_length=100)
    date = models.DateField("Date of publish")
