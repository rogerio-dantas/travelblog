from django.contrib.gis import admin

from .models import Post


class PostAdmin(admin.GeoModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
