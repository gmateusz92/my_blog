# Generated by Django 4.1.3 on 2022-11-07 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topics',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]