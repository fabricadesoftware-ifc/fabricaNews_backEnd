from django.contrib import admin

from core.models import (
    Category,
    Feeling,
    NewsFeel,
    Comments,
    News,
    Favorites,
    Reaction,
    SaveToRead,
)

from user.models import (
    User,
    UserInteractions,
    UserProjectFollow,
    Project,
)

admin.site.register(Category)
admin.site.register(Feeling)
admin.site.register(NewsFeel)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(News)
admin.site.register(UserInteractions)
admin.site.register(Favorites)
admin.site.register(Reaction)
admin.site.register(SaveToRead)
admin.site.register(Project)
admin.site.register(UserProjectFollow)
