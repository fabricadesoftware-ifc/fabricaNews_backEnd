from django.contrib import admin

from core.models import Category, Feeling, NewsFeel, User, Comments, News, UserInteractions, UserProjectFollow

admin.site.register(Category)
admin.site.register(Feeling)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(NewsFeel)
admin.site.register(News)
admin.site.register(UserInteractions)
admin.site.register(UserProjectFollow)