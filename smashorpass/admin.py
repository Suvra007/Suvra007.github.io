from django.contrib import admin

# Register your models here.
from .models import Post,Project
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post,PostAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'description']
admin.site.register(Project,ProjectAdmin)
