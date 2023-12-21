# Generated by Django 4.2.4 on 2023-09-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "users",
            "0002_alter_user_options_remove_user_username_user_avatar_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[("visitor", "visitor"), ("moderator", "moderator")],
                max_length=20,
                null=True,
            ),
        ),
    ]