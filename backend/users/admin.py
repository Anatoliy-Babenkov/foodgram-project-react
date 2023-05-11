from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Subscribe, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username')
    search_fields = ('email', 'username')
    list_filter = ('email', 'last_name')
    ordering = ('username', )
    empty_value_display = '-пусто-'


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
