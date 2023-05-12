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

    list_display = ('author', 'name', 'cooking_time',
                    'get_favorites', 'get_ingredients')
    search_fields = ('name', 'author__email', 'author__username')
    list_filter = ('tags', )
    inlines = (IngredientInline, )
    empty_value_display = '-пусто-'

    def get_favorites(self, obj):
        """Получение избранного."""
        return obj.favorites.count()
    get_favorites.short_description = 'Избранное'

    def get_ingredients(self, obj):
        """Получение ингридиентов."""
        return ', '.join(ingredients.name for ingredients
                         in obj.ingredients.all())
    get_ingredients.short_description = 'Ингридиенты'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Администрирование управление ингридиентами."""

    list_display = ('name', 'measurement_unit')
    search_fields = ('name', )
    list_filter = ('measurement_unit', )
    empty_value_display = '-пусто-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Администрирование управление тегами."""

    list_display = ('name', 'color', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', )
    empty_value_display = '-пусто-'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Администрирование управление подписками."""

    list_display = ('user__email', 'user__username', 'recipe')
    list_filter = ('recipe__tags', )
    search_fields = ('user__email', 'user__username', 'recipe')
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Администрирование списка покупок."""

    list_display = ('user__email', 'user__username', 'recipe')
    list_filter = ('recipe__tags', )
    search_fields = ('user__email', 'user__username', 'recipe')
    empty_value_display = '-пусто-'
