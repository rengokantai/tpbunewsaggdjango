from django.contrib import admin

# Register your models here.

from .models import Feed,Article
admin.site.register(Feed)
admin.site.register(Article)
