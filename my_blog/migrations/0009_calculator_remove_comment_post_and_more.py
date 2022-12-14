# Generated by Django 4.1.3 on 2022-11-08 12:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0008_alter_comment_options_remove_comment_commentator_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_1', models.IntegerField()),
                ('value_2', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_blog.topics'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default=datetime.datetime(2022, 11, 8, 12, 11, 33, 441480, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
