from django.contrib import admin
from projects.models import Project

# Register your models here.
admin.site.register(Project)

# Admin area customizations
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Snazzy Site Title"
admin.site.index_title = "Index Title"
