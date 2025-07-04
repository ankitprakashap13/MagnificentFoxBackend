# Generated by Django 5.1.7 on 2025-06-29 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_editorial_pick",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="EditorialPick",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.product"
                    ),
                ),
            ],
            options={
                "unique_together": {("product",)},
            },
        ),
    ]
