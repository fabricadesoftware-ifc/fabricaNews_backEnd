from django.contrib import admin

from core.models import Category, Feeling, User, NewsFeel

admin.site.register(Category)
admin.site.register(Feeling)
admin.site.register(User)
admin.site.register(NewsFeel)

