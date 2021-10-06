from django.db import models


# Create your models here.
class Tweet(models.Model):
    name = models.CharField(max_length=32)
    content = models.CharField(max_length=50)
    creation_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["creation_time","name"]
