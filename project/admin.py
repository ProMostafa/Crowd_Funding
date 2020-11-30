from django.contrib import admin
from .models import Project ,Category, FeatureProject
# Register your models here.
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(FeatureProject)
