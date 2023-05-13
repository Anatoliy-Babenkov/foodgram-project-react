from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Subscribe, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('is_staff', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', )
    ordering = ('username', )
    empty_value_display = '-пусто-'

    def is_staff(self, obj):
        """Получение почты автора."""
        return obj.is_staff
    is_staff.short_description = "Администратор"


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_user_email', 'author', 'get_author_email')
    search_fields = ('get_user_email',
                     'user',
                     'get_author_email',
                     'author')

    def get_author_email(self, obj):
        """Получение  почты автора."""
        return obj.author.email
    get_author_email.short_description = "Почта автора"

    def get_user_email(self, obj):
        """Получение почты автора."""
        return obj.user.email
    get_user_email.short_description = "Почта пользователя"
