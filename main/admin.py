from django.contrib import admin
from .models import Project, Recommended, Comingsoon

# Register your models here.
admin.site.register(Project)
admin.site.register(Recommended)
admin.site.register(Comingsoon)