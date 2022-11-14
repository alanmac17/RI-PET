from django.contrib import admin
from .models import DeathNotice, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(DeathNotice)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
