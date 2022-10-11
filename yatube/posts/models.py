from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    # Модель для сообществ
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="URL")
    description = models.TextField(verbose_name="Описание")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Post(models.Model):
    # Модель для поста
    text = models.TextField(
        verbose_name="Текст", help_text="Текст вашего поста"
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации", auto_now_add=True, db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор",
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="Группа",
        help_text="Группа, к которой будет относиться пост",
    )
    image = models.ImageField("Картинка", upload_to="posts/", blank=True)

    def __str__(self) -> str:
        return self.text[:15]

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    # Модель для комментария
    text = models.TextField(
        verbose_name="Текст комментария",
        help_text="Напишите свой комментарий",
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации", auto_now_add=True, db_index=True
    )
    post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, null=True, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="comments"
    )

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )
