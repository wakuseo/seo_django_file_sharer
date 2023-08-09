from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.text