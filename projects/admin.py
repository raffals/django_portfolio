from django.contrib import admin
from projects.models import Project, SlideShowProject, Slide

# Register your models here.
admin.site.register(Project)
admin.site.register(SlideShowProject)
admin.site.register(Slide)
>>>>>>> refs/remotes/origin/master

# Admin area customizations
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Snazzy Site Title"
admin.site.index_title = "Index Title"
