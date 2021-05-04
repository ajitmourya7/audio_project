from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class Song(models.Model):
    TYPE = 'song'
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateField(auto_now_add=True)


class Podcast(models.Model):
    TYPE = 'podcast'
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participants = models.CharField(max_length=1009, blank=True)


class Audiobook(models.Model):
    TYPE = 'audiobook'
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    uploaded_time = models.DateField(auto_now_add=True)


AUDIO_FILE_TYPE = [Song.TYPE, Podcast.TYPE, Audiobook.TYPE]
