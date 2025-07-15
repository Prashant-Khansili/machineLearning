from django.contrib import admin
from .models import LemonImage

@admin.register(LemonImage)
class LemonImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'prediction', 'confidence', 'uploaded_at')
    list_filter = ('prediction', 'uploaded_at')
    search_fields = ('prediction',)
    readonly_fields = ('prediction', 'confidence', 'uploaded_at')
