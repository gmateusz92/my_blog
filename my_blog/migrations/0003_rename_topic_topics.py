# Generated by Django 4.1.3 on 2022-11-06 16:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_blog', '0002_alter_topic_owner'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Topics',
        ),
    ]
