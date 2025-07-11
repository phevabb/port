# Generated by Django 5.1.3 on 2025-07-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                (
                    "tag",
                    models.CharField(
                        choices=[
                            ("API", "API"),
                            ("full_stack", "Full Stack"),
                            ("ML", "Machine Learning"),
                            ("NLP", "Natural Language Processing"),
                            ("computer_vision", "Computer Vision"),
                            ("mobile", "Mobile"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "image_alt",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Image Alt Text",
                    ),
                ),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Project Title",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Project Description"
                    ),
                ),
                (
                    "tag_1",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Project Tags",
                    ),
                ),
                (
                    "tag_2",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Project Tags",
                    ),
                ),
                (
                    "tag_3",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Project Tags",
                    ),
                ),
            ],
        ),
    ]
