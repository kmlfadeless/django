# Generated by Django 2.1.2 on 2018-10-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image_big',
            field=models.ImageField(null=True, upload_to='products/big'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_medium',
            field=models.ImageField(null=True, upload_to='products/medium'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_small',
            field=models.ImageField(null=True, upload_to='products/small'),
        ),
        migrations.AlterField(
            model_name='product',
            name='alt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
