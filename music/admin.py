from django.contrib import admin

from .models import Album,Music


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title','lyrics','alb_re']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name','author','publish_year','style']
