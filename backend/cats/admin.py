from django.contrib import admin

from .models import Achievement, Cat


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class CatAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'color', 'birth_year', 'owner', 'image')
    search_fields = ('name', 'owner')
    list_filter = ('birth_year',)
    empty_value_display = '-пусто-'


admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Cat, CatAdmin)
