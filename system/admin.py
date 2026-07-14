from django.contrib import admin
from .models import Category, Phrase, Person


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'created_at']
    list_editable = ['order']
    ordering = ['order']


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ['text', 'category', 'order', 'created_at']
    list_filter = ['category']
    search_fields = ['text']
    list_editable = ['order', 'category']
    ordering = ['category', 'order']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'relation', 'order', 'created_at']
    search_fields = ['name', 'relation']
    list_editable = ['order', 'relation']
    ordering = ['order']
