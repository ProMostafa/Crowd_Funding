from django.contrib import admin
from .models import Project ,Category, ProjectPicture,Rate, CommentReport, ProjectReport
# Register your models here.


class ProjectImageInline(admin.TabularInline):
    model = ProjectPicture


class ProductAdmin(admin.ModelAdmin):
    # list_display = ('id', 'product', 'image')
    list_filter = ('is_featured',)
    inlines = [ProjectImageInline]


class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'rating', 'created_at')


admin.site.register(Project, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProjectPicture)
admin.site.register(Rate, RateAdmin)
admin.site.register(CommentReport)
admin.site.register(ProjectReport)
