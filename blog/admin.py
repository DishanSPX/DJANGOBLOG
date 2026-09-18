from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        css = {
            "all": ("blog/css/admin.css",)
        }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)