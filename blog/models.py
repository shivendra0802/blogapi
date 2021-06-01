from django.db import models

# Create your models here.
class Post(models.Model):
    title              =        models.CharField(max_length=255)
    description        =        models.TextField()
    content            =        models.TextField()
    date_created       =        models.DateTimeField(auto_now_add=True)
    date_updated       =        models.DateTimeField(auto_now=True)
    category           =        models.CharField(max_length=200)


    def __str__(self):
        return self.title