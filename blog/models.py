from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

#要先发布一个post查询集才能返回所有的，为什么？

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title