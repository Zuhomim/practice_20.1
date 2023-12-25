from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    preview = models.ImageField(upload_to="blog/", **NULLABLE, verbose_name='Предпросмотр')
    created_at = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'
