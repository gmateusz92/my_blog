from django.db import models
from django.contrib.auth.models import User


class Topics(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

class Comment(models.Model):

    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    #commentator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.body