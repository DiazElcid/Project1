# Generated by Django 4.1.5 on 2023-02-03 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todo_list", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="사용자",
            ),
        ),
    ]
