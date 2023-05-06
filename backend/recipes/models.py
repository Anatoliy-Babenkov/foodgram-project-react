from colorfield.fields import ColorField
from django.conf import settings as s
from django.core.validators import (MinValueValidator, RegexValidator)
from django.db import models
from django.db.models import UniqueConstraint

from users.models import User


class Ingredient(models.Model):
    """Модель ингридиентов."""

    name = models.CharField(max_length=s.RECIPE_NAME,
                            db_index=True,
                            verbose_name='Название ингридиента')
    measurement_unit = models.CharField(max_length=s.RECIPE_NAME,
                                        verbose_name='Единицы измерения')

    class Meta():
        ordering = ('name', )
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        constraints = (models.UniqueConstraint(
            fields=('name', 'measurement_unit'),
            name='unique_name_measurement_unit'), )

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    """Модель тегов."""

    color = ColorField(unique=True,
                       verbose_name='HEX-код',
                       format='hex',
                       max_length=s.HEX_NAME,
                       validators=(RegexValidator(
                           regex="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                           message='Проверьте введённые данные'), ))
    name = models.CharField(max_length=s.RECIPE_NAME,
                            unique=True,
                            db_index=True,
                            verbose_name='Название тега')
    slug = models.SlugField(unique=True,
                            verbose_name='Slug')

    class Meta:
        ordering = ('name', )
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель рецептов."""

    ingredients = models.ManyToManyField(Ingredient,
                                         verbose_name='Ингридиенты',
                                         through='IngredientRecipe')
    tags = models.ManyToManyField(Tag,
                                  verbose_name='Теги')
    image = models.ImageField('Картинка', upload_to='recipes/')
    name = models.CharField('Название рецепта', max_length=s.RECIPE_NAME)
    text = models.TextField('Описание')
    cooking_time = models.PositiveSmallIntegerField(
        'Время готовки',
        validators=(MinValueValidator(
            s.MIN_COOKING_TIME,
            message='Время приготовления не должно быть менее 1 минуты!'), ))
    author = models.ForeignKey(User,
                               null=True,
                               verbose_name='Автор',
                               on_delete=models.SET_NULL,
                               related_name='recipes')

    class Meta:
        ordering = ('-id', )
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class BaseFavoriteShoppingCart(models.Model):
    """Модель списка покупок и избранного."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )

    class Meta:
        abstract = True
        constraints = (
            UniqueConstraint(fields=('user', 'recipe'),
                             name='%(app_label)s_%(class)s_unique'), )

    def __str__(self):
        return f'{self.user} :: {self.recipe}'


class Favorite(BaseFavoriteShoppingCart):
    """Модель избраного."""

    class Meta(BaseFavoriteShoppingCart.Meta):
        default_related_name = 'favorites'
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingCart(BaseFavoriteShoppingCart):
    """Модель корзины покупок."""

    class Meta(BaseFavoriteShoppingCart.Meta):
        default_related_name = 'shopping_list'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class IngredientRecipe(models.Model):
    """Модель ингридиенты рецепта."""

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
        related_name='recipetoingredients'
    )
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='ingredienttorecipe'
    )
    amount = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(s.MIN_AMOUNT_INGREDIENTS), ),
        verbose_name='Объём ингредиента'
    )

    class Meta:
        ordering = ('-id', )
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return (
            f'{self.ingredient.name} ({self.ingredient.measurement_unit})'
            f' - {self.amount} ')
