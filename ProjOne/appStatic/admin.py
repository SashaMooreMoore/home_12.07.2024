from django.contrib import admin
from .models import FormHelp, InfoNews
from django_summernote.admin import SummernoteModelAdmin


@admin.register(FormHelp)
class FormHelpAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dtime', 'status']
    list_display_links = ['id', 'name', 'dtime']
    list_filter = ['dtime', 'status']
    list_editable = ['status']
    list_per_page = 20
    

@admin.register(InfoNews)
class InfoNews(SummernoteModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    summernote_fields = ('content',)