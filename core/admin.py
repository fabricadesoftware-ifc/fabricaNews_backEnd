from django.contrib import admin

from core.models import Category, Feeling, NewsFeel, User, Comments, News, UserInteractions, Favorites, Save_to_read, Project, UserProjectFollow

admin.site.register(Category)
admin.site.register(Feeling)
admin.site.register(NewsFeel)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(News)
admin.site.register(UserInteractions)
admin.site.register(Favorites)
admin.site.register(Save_to_read)
admin.site.register(Project)
admin.site.register(UserProjectFollow)