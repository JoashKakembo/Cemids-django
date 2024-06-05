from django.contrib import admin
from .models import EducationalContent

@admin.register(EducationalContent)
class EducationalContentAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'author', 'description')
    search_fields = ('subtitle', 'author', 'description')
    list_filter = ('author',)
