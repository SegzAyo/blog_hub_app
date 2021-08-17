from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    intro = models.CharField(max_length=255)
    body = models.TextField(max_length=700)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(max_length=400)
    date_added = models.DateTimeField(auto_now_add=True)
