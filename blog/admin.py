from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_time', 'update_time', 'category', 'author']
admin.site.register(Post, PostAdmin)
class CatAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
admin.site.register(Category, CatAdmin)
admin.site.register(Tag)