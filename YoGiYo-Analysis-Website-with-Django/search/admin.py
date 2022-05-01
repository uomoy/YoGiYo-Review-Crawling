from django.contrib import admin

from search.models import MenuAnalysis, MenuImg, Wordclouds, Restaurants, Menus
# Register your models here.

admin.site.register(MenuAnalysis)
admin.site.register(MenuImg)
admin.site.register(Wordclouds)
admin.site.register(Restaurants)
admin.site.register(Menus)