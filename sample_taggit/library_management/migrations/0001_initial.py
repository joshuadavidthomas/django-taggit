# Generated by Django 5.0.6 on 2024-07-28 14:49

import uuid

import django.db.models.deletion
from django.db import migrations, models

import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="BookType",
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
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        max_length=100,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name": "Book Type",
                "verbose_name_plural": "Book Types",
            },
        ),
        migrations.CreateModel(
            name="ConditionTag",
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
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="name"),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        max_length=100,
                        unique=True,
                        verbose_name="slug",
                    ),
                ),
            ],
            options={
                "verbose_name": "Condition Tag",
                "verbose_name_plural": "Condition Tags",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Author",
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
                ("first_name", models.CharField(blank=True, max_length=255)),
                ("last_name", models.CharField(blank=True, max_length=255)),
                ("middle_name", models.CharField(blank=True, max_length=255)),
                ("birth_date", models.DateField()),
                ("biography", models.TextField()),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=255)),
                ("published_date", models.DateField(null=True)),
                ("isbn", models.CharField(max_length=17, unique=True)),
                ("summary", models.TextField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library_management.author",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Book",
                "verbose_name_plural": "Books",
            },
        ),
        migrations.CreateModel(
            name="Magazine",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("library_management.book",),
        ),
        migrations.CreateModel(
            name="ConditionTaggedItem",
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
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="library_management.conditiontag",
                    ),
                ),
            ],
            options={
                "verbose_name": "Condition Tagged Item",
                "verbose_name_plural": "Condition Tagged Items",
            },
        ),
        migrations.CreateModel(
            name="PhysicalCopy",
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
                    "barcode",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="physical_copies",
                        to="library_management.book",
                    ),
                ),
                (
                    "book_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library_management.booktype",
                    ),
                ),
                (
                    "condition_tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="library_management.ConditionTaggedItem",
                        to="library_management.ConditionTag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Physical Copy",
                "verbose_name_plural": "Physical Copies",
            },
        ),
        migrations.AddField(
            model_name="conditiontaggeditem",
            name="content_object",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="library_management.physicalcopy",
            ),
        ),
    ]
