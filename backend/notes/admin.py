from django.contrib import admin
from .models import Insight, Category


admin.site.register(Category)


class InsightAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'caption',
        'source_url',
        'visible',
        'updated_at',
    ]
    search_fields = ['caption', 'category']
    list_filter = ['category', 'updated_at', 'visible']
    ordering = ['-updated_at']


admin.site.register(Insight, InsightAdmin)
