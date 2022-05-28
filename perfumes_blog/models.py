from django.db import models
from django.contrib. auth import get_user_model
# Create your models here.

class Perfume(models.Model):
    perfume_name = models.CharField(max_length=255)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    perfume_price = models.IntegerField(max_length=155,default=0)
    perfume_edition = models.CharField(max_length=255)
    perfume_size = models.IntegerField(max_length=55, default=0)
    perfume_description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.perfume_name