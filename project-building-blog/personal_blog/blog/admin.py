from django.contrib import admin
from .models import Author, Tag, Post, Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_add')
    search_fields = ('first_name', 'last_name', 'email_add')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'excerpt', 'date', 'author', 'tag_list')
    search_fields = ('title', 'excerpt', 'content')
    filter_horizontal = ('tag',)
    prepopulated_fields = {"slug": ("title", )}

    def tag_list(self, obj):
        return ', '.join([tag.name for tag in obj.tag.all()])

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment_content', 'post')
    search_fields = ('author', 'post')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

