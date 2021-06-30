from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.CharField()
    body = models.CharField(max_length=700)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']