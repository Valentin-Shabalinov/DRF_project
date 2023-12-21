# Generated by Django 4.2.4 on 2023-09-18 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("education", "0013_remove_payment_payment_intent_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="is_paid",
            field=models.BooleanField(default=False, verbose_name="оплачено"),
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_intent_id",
            field=models.CharField(
                default="NULL", max_length=100, verbose_name="id_платежа"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Безналичный", "Безналичный"),
                    ("Наличные", "Наличные"),
                ],
                default="Безналичный",
                max_length=100,
                null=True,
                verbose_name="Способ оплаты",
            ),
        ),
    ]
