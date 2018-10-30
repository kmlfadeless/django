# Generated by Django 2.1.2 on 2018-10-30 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181026_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_big',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_medium',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_small',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='images.Image'),
        ),
    ]
