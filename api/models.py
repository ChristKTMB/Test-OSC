from django.db import models

# Create your models here.
    
from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
