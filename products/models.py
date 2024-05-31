from django.db import models
from django.utils.text import slugify
from googletrans import Translator


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    text = models.TextField(max_length=250, blank=True, verbose_name='Описание')
    datedb = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Slug')
    image = models.ImageField(upload_to='photos/', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Все товары'
        verbose_name_plural = 'Все товары'
        ordering = ['-datedb']

    def save(self, *args, **kwargs):
        if not self.slug:
            translator = Translator()
            translation = translator.translate(self.title, dest='en')
            self.slug = slugify(translation.text)
            unique_slug = self.slug
            num = 1
            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug

        super(Product, self).save(*args, **kwargs)


class ProductType(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prods', verbose_name='Категория ')
    title = models.CharField(max_length=60, verbose_name='Название')
    text = models.TextField(max_length=50, blank=True, verbose_name='Описание')
    datedb = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Slug')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    image = models.ImageField(upload_to='photos/', blank=True, verbose_name='Картинка')

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ['-datedb']

    def save(self, *args, **kwargs):
        if not self.slug:
            translator = Translator()
            translation = translator.translate(self.title, dest='en')
            self.slug = slugify(translation.text)
            unique_slug = self.slug
            num = 1
            while ProductType.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
            self.slug = unique_slug

        super(ProductType, self).save(*args, **kwargs)
