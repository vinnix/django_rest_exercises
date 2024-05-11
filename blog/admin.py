from django.contrib import admin

# Register your models here.

# blog/admin.py

from blog.models import Category, Article


admin.site.register(Category)
admin.site.register(Article)


