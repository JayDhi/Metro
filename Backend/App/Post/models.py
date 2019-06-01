# App/Post/models.py
# import from framework
from django.db import models
# import from project

class Post(models.Model):
    post_title = models.CharField(max_length=20)
    post_body = models.CharField(max_length=200)
    post_linkn = models.URLField(max_length=250)
    def __str__(self):
        return self.post_title