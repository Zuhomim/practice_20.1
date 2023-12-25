from django.contrib import admin


from blog.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'is_published', 'created_at',)
    list_filter = ('title',)
    search_fields = ('title', 'content')

