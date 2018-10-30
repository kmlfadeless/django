from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(
        max_length=255,
    )
    snippet = models.TextField(
        blank=True,
        null=True,
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(
        max_length=255,
    )
    url_key = models.CharField(
        max_length=255,
        # @todo make unique
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    image_small = models.ImageField(
        upload_to='products/small',
        null=True,
    )
    image_medium = models.ImageField(
        upload_to='products/medium',
        null = True,
    )
    image_big = models.ImageField(
        upload_to='products/big',
        null=True,
    )
    alt = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    characteristics = models.TextField(
        blank=True,
        null=True,
    )
    details = models.TextField(
        blank=True,
        null=True,
    )
    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


