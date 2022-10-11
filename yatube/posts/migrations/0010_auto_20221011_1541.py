# Generated by Django 2.2.16 on 2022-10-11 12:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0009_follow"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="created",
        ),
        migrations.RemoveField(
            model_name="follow",
            name="created",
        ),
        migrations.AddField(
            model_name="comment",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True,
                db_index=True,
                default=django.utils.timezone.now,
                verbose_name="Дата публикации",
            ),
            preserve_default=False,
        ),
    ]
