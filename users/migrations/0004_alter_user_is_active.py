# Generated by Django 4.2.4 on 2023-09-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True, verbose_name="Активность пользователя"
            ),
        ),
    ]