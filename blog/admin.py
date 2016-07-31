from django.contrib import admin
from blog.models import Post, Comment, Tag, Contact, PostCode


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']

admin.site.register(Post, PostAdmin)


admin.site.register(Comment)


admin.site.register(Tag)


admin.site.register(Contact)


admin.site.register(PostCode)