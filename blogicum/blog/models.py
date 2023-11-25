
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Location(models.Model):
    """Represents a location."""

    name = models.CharField(
        verbose_name='Название места',
        max_length=256
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True
    )

    class Meta:
        """Returns a string representation of the model."""

        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Category(models.Model):
    """Represents a category."""

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.'),
        unique=True
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True
    )

    class Meta:
        """Returns a string representation of the model."""

        verbose_name = 'категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Post(models.Model):
    """Represents a post."""

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        auto_now_add=False,
        help_text=('Если установить дату и время в будущем — '
                   'можно делать отложенные публикации.')
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(
        Location,
        verbose_name='Местоположение',
        on_delete=models.SET_NULL,
        null=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True

    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True
    )

    class Meta:
        """Returns a string representation of the model."""

        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
