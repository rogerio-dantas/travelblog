from django.contrib.gis import admin

from . import models


class ImageInLine(admin.StackedInline):
    model = models.Image


class PostAdmin(admin.GeoModelAdmin):
    inlines = [ImageInLine]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Post, PostAdmin)
