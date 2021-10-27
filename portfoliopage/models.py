from django.db import models
# from embed_video.fields import EmbedVideoField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class TravelingPost(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    #thumbnail
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags= models.ManyToManyField(Tag, null=True)
    # youtubeVideo = EmbedVideoField()  # same like models.URLField()
    # slug = 

    def __str__(self):
        return self.headline

