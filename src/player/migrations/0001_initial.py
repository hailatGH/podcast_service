# Generated by Django 4.1 on 2022-10-27 13:40

import core.validators
from django.db import migrations, models
import django.db.models.deletion
import player.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoriesModel",
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
                ("category_name", models.CharField(blank=True, max_length=256)),
                (
                    "category_rating",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("category_status", models.BooleanField(blank=True, default=False)),
                (
                    "category_description",
                    models.CharField(blank=True, max_length=4096, null=True),
                ),
                ("category_viewcount", models.IntegerField(blank=True, default=0)),
                (
                    "category_coverImage",
                    models.ImageField(
                        blank=True,
                        upload_to=player.models.Categories_Cover_Images,
                        validators=[core.validators.validate_image_extension],
                    ),
                ),
                ("encoder_FUI", models.CharField(blank=True, max_length=1023)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="HostsModel",
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
                ("host_name", models.CharField(blank=True, max_length=256)),
                ("host_title", models.CharField(blank=True, max_length=256, null=True)),
                ("host_rating", models.IntegerField(blank=True, default=0, null=True)),
                ("host_status", models.BooleanField(blank=True, default=False)),
                (
                    "host_description",
                    models.CharField(blank=True, max_length=4096, null=True),
                ),
                ("host_viewcount", models.IntegerField(blank=True, default=0)),
                (
                    "host_profileImage",
                    models.ImageField(
                        blank=True,
                        upload_to=player.models.Hosts_Cover_Images,
                        validators=[core.validators.validate_image_extension],
                    ),
                ),
                (
                    "host_FUI",
                    models.CharField(blank=True, max_length=1023, unique=True),
                ),
                ("encoder_FUI", models.CharField(blank=True, max_length=1023)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="PodcastsModel",
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
                ("podcast_name", models.CharField(blank=True, max_length=256)),
                (
                    "podcast_rating",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("podcast_status", models.BooleanField(blank=True, default=False)),
                (
                    "podcast_description",
                    models.CharField(blank=True, max_length=4096, null=True),
                ),
                ("podcast_viewcount", models.IntegerField(blank=True, default=0)),
                (
                    "podcast_coverImage",
                    models.ImageField(
                        blank=True,
                        upload_to=player.models.Podcasts_Cover_Images,
                        validators=[core.validators.validate_image_extension],
                    ),
                ),
                ("encoder_FUI", models.CharField(blank=True, max_length=1023)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="podcast_category",
                        to="player.categoriesmodel",
                    ),
                ),
                (
                    "host",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="podcast_host",
                        to="player.hostsmodel",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="SeasonsModel",
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
                ("season_name", models.CharField(blank=True, max_length=256)),
                (
                    "season_rating",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("season_status", models.BooleanField(blank=True, default=False)),
                ("season_releaseDate", models.DateField(blank=True, null=True)),
                (
                    "season_description",
                    models.CharField(blank=True, max_length=4096, null=True),
                ),
                ("season_viewcount", models.IntegerField(blank=True, default=0)),
                (
                    "season_coverImage",
                    models.ImageField(
                        blank=True,
                        upload_to=player.models.Seasons_Cover_Images,
                        validators=[core.validators.validate_image_extension],
                    ),
                ),
                ("season_price", models.IntegerField(blank=True, default=40)),
                ("encoder_FUI", models.CharField(blank=True, max_length=1023)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "podcast",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="season_podcast",
                        to="player.podcastsmodel",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="EpisodesModel",
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
                ("episode_name", models.CharField(blank=True, max_length=256)),
                (
                    "episode_rating",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("episode_status", models.BooleanField(blank=True, default=False)),
                ("episode_releaseDate", models.DateField(blank=True, null=True)),
                (
                    "episode_description",
                    models.CharField(blank=True, max_length=4096, null=True),
                ),
                ("episode_viewcount", models.IntegerField(blank=True, default=0)),
                (
                    "episode_coverImage",
                    models.ImageField(
                        blank=True,
                        upload_to=player.models.Episode_Cover_Images,
                        validators=[core.validators.validate_image_extension],
                    ),
                ),
                (
                    "episode_audioFile",
                    models.FileField(
                        blank=True,
                        upload_to=player.models.Episode_Files,
                        validators=[core.validators.validate_episode_extension],
                    ),
                ),
                ("episode_price", models.IntegerField(blank=True, default=5)),
                ("encoder_FUI", models.CharField(blank=True, max_length=1023)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="episode_category",
                        to="player.categoriesmodel",
                    ),
                ),
                (
                    "host",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="episode_host",
                        to="player.hostsmodel",
                    ),
                ),
                (
                    "podcast",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="episode_podcast",
                        to="player.podcastsmodel",
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="episode_season",
                        to="player.seasonsmodel",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]