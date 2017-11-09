from django.db import models
from django.utils import timezone

import markdown


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    content_html = models.TextField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published_at', '-id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content_html = markdown.markdown(self.content)
        super().save(*args, **kwargs)
