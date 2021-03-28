from typing import Reversible
from project.settings import TIME_ZONE
from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    
    title = models.CharField( max_length=50)
    content =  models.TextField(max_length=1500)
    created_at = models.DateField(default=timezone.now)
    image = models.ImageField( upload_to = 'post-img/' )
    

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return Reversible("Post_detail", kwargs={"pk": self.pk})
