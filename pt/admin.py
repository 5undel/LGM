from django.contrib import admin
from .models import TraningCategory, Coach

# Register your models here.
class TraningCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
    )

    ordering = ('name',)

class CoachAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(TraningCategory)
admin.site.register(Coach)