from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    project_link = models.URLField()

    # Print project title in admin interface (doensn't work)
    def __str__(self):
        return self.title  # or any of the other appropriate variables
    
