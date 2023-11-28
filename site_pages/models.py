from django.db import models

# site_pages/models.py
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
# site_pages/models.py
from django.db import models

class RecipeBlog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateField()

    def __str__(self):
        return self.title


# Create your models here.
