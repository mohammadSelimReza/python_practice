from django.db import models

class MusicianModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12, blank=True, null=True)
    instrument_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
