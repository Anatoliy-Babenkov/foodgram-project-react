from django.contrib import admin
from recipes.models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                            ShoppingCart, Tag)


class IngredientInline(admin.TabularInline):
    model = IngredientRecipe
    extra = 3
    min_num = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Администрирование рецептов."""

    list_display = ('author',
                    'get_author_email',
                    'name',
                    'cooking_time',
                    'get_favorites',
                    'get_ingredients')
    search_fields = ('name', 'author', 'get_author_email')
    list_filter = ('tags', )
    inlines = (IngredientInline, )

    def get_author_email(self, obj):
        """Получение почты автора."""
        return obj.author.email
    get_author_email.short_description = "Почта автора"

    def get_favorites(self, obj):
        """Получение количества в избранном у пользователей."""
        return obj.favorites.count()
    get_favorites.short_description = 'Избранное'

    def get_ingredients(self, obj):
        """Получение списка ингридиентов."""
        return ', '.join(ingredients.name for ingredients
                         in obj.ingredients.all())
    get_ingredients.short_description = 'Ингридиенты'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Администрирование управление ингридиентами."""

    list_display = ('name', 'measurement_unit')
    search_fields = ('name', )
    list_filter = ('measurement_unit', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Администрирование управление тегами."""

    list_display = ('name', 'color', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Администрирование управление подписками."""

    list_display = ('recipe', 'get_user_email', 'user')
    list_filter = ('get_recipe_tag', )
    search_fields = ('recipe', 'user__email', 'user')

    def get_user_email(self, obj):
        """Получение почты пользователя."""
        return obj.user.email
    get_user_email.short_description = "Почта пользователя"

    def get_recipe_tag(self, obj):
        """Получение тега рецепта."""
        return obj.recipe.tags
    get_recipe_tag.short_description = "Тег"


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Администрирование списка покупок."""

    list_display = ('recipe', 'get_user_email', 'user')
    list_filter = ('get_recipe_tag', )
    search_fields = ('recipe', 'user__email', 'user')

    def get_user_email(self, obj):
        """Получение почты пользователя."""
        return obj.user.email
    get_user_email.short_description = "Почта пользователя"

    def get_recipe_tag(self, obj):
        """Получение тега рецепта."""
        return obj.recipe.tags
    get_recipe_tag.short_description = "Тег"
