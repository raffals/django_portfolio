from django.db import models

class Project(models.Model):
    def __str__(self):  # Print project title in admin interface
        return self.title  # or any of the other appropriate variables
    class Meta:
        ordering = ['order']
    
    order = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    technology = models.TextField(default='')
    image = models.CharField(max_length=100)
    project_link = models.URLField(blank=True)  # Hyperlink to live app hosted elsewhere

class VideoProject(models.Model):
    def __str__(self):  # Print project title in admin interface
        return self.title  # or any of the other appropriate variables
    class Meta:
        ordering = ['order']
    
    order = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    technology = models.TextField(default='')
    image = models.CharField(max_length=100)
    video = models.CharField(max_length=100)  # Hosted video file
    video_link = models.URLField(blank=True)  # Hyperlink to video hosted elsewhere

class SlideShowProject(models.Model):
    def __str__(self):  # Print project title in admin interface
        return self.title  # or any of the other appropriate variables
    class Meta:
        ordering = ['order']

    order = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    technology = models.TextField(default='')
    image = models.CharField(max_length=100)

class Slide(models.Model):
    def __str__(self):  # Print slide title in admin interface
        return self.project.title.upper() + " - " + self.title
    class Meta:
        ordering = ['project', 'order']

    project = models.ForeignKey(SlideShowProject, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    image = models.CharField(max_length=100)
