from django.contrib import admin
from BloggingApp.models import Post
from BloggingApp.models import Comments

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','publish','created')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}
admin.site.register(Post,PostAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display=['post','name','email','body','created','updated','active']
    list_filter=('active','created','updated')
    search_fields=('name''email','body')

admin.site.register(Comments,CommentsAdmin)