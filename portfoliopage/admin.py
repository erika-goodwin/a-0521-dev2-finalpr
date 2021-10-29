from django.contrib import admin

# Register your models here.

from .models import TravelingPost, Tag, SnowboardingPost

admin.site.register(TravelingPost)
admin.site.register(SnowboardingPost)
admin.site.register(Tag)
