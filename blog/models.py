from django.db import models


class Stories(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=60)
    image = models.ImageField(upload_to="posts", null=True)
    plot = models.TextField()


class Subscription(models.Model):
    user_email = models.EmailField()
