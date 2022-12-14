# blog/admin.py
"""
The blog app admin definitions.
"""
from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    """
    The Post Admin Class setup to manage posts via the admin console.
    """
    list_display = (
        'title',
        'author',
        'status',
        'created',
        'updated',
    )

    list_filter = (
        'status',
        'topics',
    )

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    The Topics Admin created to enable topics through the admin console.
    """
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Post, PostAdmin)

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'name',
        'email',
        'created'
    )
    list_filter = (
        'post',
        'name',
        'email',
        'created'
    )

    search_fields = (
        'post',
        'name',
        'email',
        'text'
    )

