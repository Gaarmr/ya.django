from django.contrib import admin

from .models import Group, Post


class PostAdmin(admin.ModelAdmin):                                  # перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "text", "pub_date", "author", "group")    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",)                                       # добавляем возможность фильтрации по дате
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"                                 # это свойство сработает для всех колонок: где пусто - там будет эта строка

class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")
    search_fields = ("title",)
    empty_value_display = "-пусто-" 

admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)                                # при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin