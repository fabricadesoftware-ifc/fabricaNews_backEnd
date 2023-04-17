from django.contrib import admin

from core.models import Category, Feeling, User, Comments

admin.site.register(Category)
admin.site.register(Feeling)
admin.site.register(User)
admin.site.register(Comments)

