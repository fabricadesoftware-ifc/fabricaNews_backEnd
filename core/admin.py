from django.contrib import admin

from core.models import Category, Feeling, User, NewsFeel, Comments, Project
# News

admin.site.register(Category)
admin.site.register(Feeling)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(NewsFeel)
# admin.site.register(News)
admin.site.register(Comments)