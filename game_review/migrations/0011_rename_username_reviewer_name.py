# Generated by Django 5.1.3 on 2024-12-05 19:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("game_review", "0010_alter_review_rating"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reviewer",
            old_name="username",
            new_name="name",
        ),
    ]
