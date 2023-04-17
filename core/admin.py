from django.contrib import admin

from core.models import Category, Feeling, User, Comments, News, UserInteractions

admin.site.register(Category)
admin.site.register(Feeling)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(News)
admin.site.register(UserInteractions)