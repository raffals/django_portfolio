"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    # If pointed to /projects, then point forward to views.py
    path('', views.all_projects, name="all_projects"),
    # <> grabs a portion of url & pass forward to app as arg pk in
    #    views/templates (eg, to views.project_detail)
    # "int" = path converter (gives error unless there's an int at this point in path)
    path('<int:pk>', views.project_detail, name="project_detail"),
    path('v<int:pk>', views.video_project_detail, name="video_project_detail"),
    path('s<int:pk>', views.slide_project_detail, name="slide_project_detail"),
    path('s<int:pk>/slides', views.project_slides, name="project_slides"),
]
