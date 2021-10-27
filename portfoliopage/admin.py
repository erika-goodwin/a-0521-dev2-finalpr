from django.contrib import admin

# Register your models here.

from .models import TravelingPost, Tag

admin.site.register(TravelingPost)
admin.site.register(Tag)
