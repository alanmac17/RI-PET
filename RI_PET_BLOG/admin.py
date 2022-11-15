from django.contrib import admin
from .models import DeathNotice, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(DeathNotice)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'death_date')
    search_fields = ['title', 'content']
    list_filter = ('status', 'death_date')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'deathnotice', 'created_on')
    list_filter = ('created_on', 'name')
    search_fields = ('name', 'email', 'body')

