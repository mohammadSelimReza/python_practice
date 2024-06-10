from django.db import models

# Create your models here.
class FormModel(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self) -> str:
        return self.title