from django.conf import settings as s


class ErrorMessage:
    SELF_FOLLOWING_ERROR = 'Нельзя подписаться на самого себя'
    ADD_FOLLOWING_ERROR = 'Подписка уже оформлена'
    NO_TAG_ERROR = 'Нет указанного тега'
    NO_INGREDIENT_ERROR = 'Ингридиенты не указаны'
    RELAPSE_INGREDIENT_ERROR = 'Ингридиенты повторяются'
    AMOUNT_INGREDIENT_ERROR = 'Объём ингридиента не указан'
    RECIPE_IN_FAVORITE_ERROR = 'Рецепт уже в избранном'
    MIN_TIME_ERROR = ('Время готовки не должно быть менее '
                      f'{s.MIN_COOKING_TIME} минуты')
    RECIPE_IN_CART_ERROR = 'Рецепт уже в корзине'


CONTENT_TYPE = 'text/plain'
