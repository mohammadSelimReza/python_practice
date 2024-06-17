from django.db import models

# Create your models here.
class BlogModel(models.Model):
    blogTitle = models.CharField(max_length=50)
    blogDes = models.TextField()
    
    def __str__(self) -> str:
        return self.blogTitle