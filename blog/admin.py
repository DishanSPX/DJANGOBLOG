from django.contrib import admin
from .models import Category, Tag, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "category", "created_at")
    list_filter = ("status", "category", "tags")
    search_fields = ("title", "content")
    filter_horizontal = ("tags",)