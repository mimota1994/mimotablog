from django.contrib import admin

from models import Article,Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article,ArticleAdmin)


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag,TagAdmin)