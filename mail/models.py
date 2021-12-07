from django.db import models


# Create your models here.

class EmailAttachment(models.Model):
    email = models.EmailField()
    image = models.ImageField()
