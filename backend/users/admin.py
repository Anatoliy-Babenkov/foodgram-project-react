from django.contrib import admin

from users.models import Subscribe, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
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
    list_display = ('user',
                    'get_user_email',
                    'author',
                    'get_author_email')
    search_fields = ('user',
                     'user__email',
                     'author',
                     'author__email')
    empty_value_display = '-пусто-'

    def get_author_email(self, obj):
        """Получение почты автора."""
        return obj.author.email
    get_author_email.short_description = "Почта автора"

    def get_user_email(self, obj):
        """Получение почты подписчика."""
        return obj.user.email
    get_user_email.short_description = "Почта подписчика"
