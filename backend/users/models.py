from django.conf import settings as s
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from django.db import models
from django.db.models import CharField, EmailField, F, Q, UniqueConstraint


class User(AbstractUser):
    """
    Авторизованный пользователь может:

    Входить в систему под своим логином и паролем.
    Выходить из системы (разлогиниваться).
    Менять свой пароль.
    Создавать/редактировать/удалять собственные рецепты.
    Просматривать рецепты на главной.
    Просматривать страницы пользователей.
    Просматривать отдельные страницы рецептов.
    Фильтровать рецепты по тегам.
    Работать с персональным списком избранного: добавлять в него рецепты или
    удалять их, просматривать свою страницу избранных рецептов.
    Работать с персональным списком покупок: добавлять/удалять любые рецепты,
    выгружать файл с количеством необходимых ингридиентов для рецептов из
    списка покупок.
    Подписываться на публикации авторов рецептов и отменять подписку,
    просматривать свою страницу подписок.
    """

    REQUIRED_FIELDS = ('first_name', 'last_name', 'username')
    USERNAME_FIELD = 'email'
    username = CharField(max_length=s.NAME_FIELD,
                         unique=True,
                         verbose_name='Имя пользователя',
                         help_text='Имя пользователя',
                         validators=(UnicodeUsernameValidator(), ))
    email = EmailField(max_length=s.EMAIL_FIELD,
                       unique=True,
                       verbose_name='Адрес электронной почты',
                       help_text='Адрес электронной почты',
                       validators=(EmailValidator(
                           message='Некорректный email'), ))
    first_name = CharField(max_length=s.NAME_FIELD,
                           verbose_name='Имя',
                           help_text='Имя')
    last_name = CharField(max_length=s.NAME_FIELD,
                          verbose_name='Фамилия',
                          help_text='Фамилия')

    class Meta:
        ordering = ('username', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    """
    На странице:

    Имя пользователя, все рецепты, опубликованные
    пользователем и возможность подписаться на пользователя.
    """

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Подписчик',
                             related_name='follower')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор',
                               related_name='following')

    class Meta:
        ordering = ('-id', )
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (UniqueConstraint(fields=('user', 'author'),
                                        name='unique_follow'),
                       models.CheckConstraint(check=~Q(user=F('author')),
                                              name='no_self_follow'))

    def __str__(self) -> str:
        return f'{self.user} подписан на {self.author}'
