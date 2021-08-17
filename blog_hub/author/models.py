from django.db import models

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(min_lenght=8)
    occupation = models.CharField()
    email = models.EmailField(max_length=254)
    signUpDate = models.DateTimeField(auto_now_add=True)