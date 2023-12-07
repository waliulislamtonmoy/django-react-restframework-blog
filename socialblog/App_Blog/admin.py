from django.contrib import admin

from App_Blog.models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display=["author","title","date",]

admin.site.register(Blog,BlogAdmin)