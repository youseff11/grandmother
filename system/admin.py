from django.contrib import admin
from .models import Category, Phrase, Person


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'created_at']
    list_editable = ['order']
    ordering = ['order']


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    list_display = ['text', 'category', 'has_audio', 'order', 'created_at']
    list_filter = ['category']
    search_fields = ['text']
    list_editable = ['order', 'category']
    ordering = ['category', 'order']

    @admin.display(boolean=True, description='فيه تسجيل صوتي')
    def has_audio(self, obj):
        return bool(obj.audio)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'relation', 'has_audio', 'order', 'created_at']
    search_fields = ['name', 'relation']
    list_editable = ['order', 'relation']
    ordering = ['order']

    @admin.display(boolean=True, description='فيه تسجيل صوتي')
    def has_audio(self, obj):
        return bool(obj.audio)
