from django.core.exceptions import ValidationError
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    # created_at = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name="Цена 1 шт")
    created_at = models.DateTimeField(verbose_name='Дата создания')
    changed_at = models.DateTimeField(verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name="Номер версии")
    version_name = models.CharField(max_length=50, verbose_name="Название версии")
    is_current = models.BooleanField(**NULLABLE, verbose_name='Признак версии')

    def __str__(self):
        return f'{self.product} ({self.version_name})'

    def clean(self) -> None:
        super().clean()
        if Version.objects.filter(
                product=self.product,
                is_current=True
        ).exists():
            raise ValidationError('You can set only one active version.')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
