from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry
# from .models import ArtistsModel
__all__ = (
    'update_document',
    'delete_document',
)


@receiver(post_save)
def update_document(sender, **kwargs):
    """Update document on added/changed records.
    Update Book document index if related `books.Publisher` (`publisher`),
    `books.Author` (`authors`), `books.Tag` (`tags`) fields have been updated
    in the database.
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'podcast':
        # If it is `books.Publisher` that is being updated.
        if model_name == 'Episodesmodel':
            #[CategoriesModel, PodcastsModel, SeasonsModel, HostsModel]
            categoryinstances = instance.CategoriesModel.all()
            podcastinstances = instance.PodcastsModel.all()
            seasoninstances = instance.SeasonsModel.all()
            hostinstances = instance.HostsModel.all()
            for _instance in categoryinstances:
                registry.update(_instance)
            for _instance in podcastinstances:
                registry.update(_instance)
            for _instance in seasoninstances:
                registry.update(_instance)
            for _instance in hostinstances:
                registry.update(_instance)
        if model_name == 'HostsModel':
            podcastinstances = instance.PodcastsModel.all()
            episodeinstances = instance.EpisodesModel.all()
            for _instance in podcastinstances:
                registry.update(_instance)
            for _instance in episodeinstances:
                registry.update(_instance)
        if model_name == 'SeasonsModel':
            podcastinstances = instance.PodcastsModel.all()
            episodeinstances = instance.EpisodesModel.all()
            for _instance in podcastinstances:
                registry.update(_instance)
            for _instance in episodeinstances:
                registry.update(_instance)
        if model_name == 'PodcastsModel':
            categoryinstances = instance.CategoriesModel.all()
            episodeinstances = instance.EpisodesModel.all()
            seasoninstances = instance.SeasonsModel.all()
            hostinstances = instance.HostsModel.all()
            for _instance in categoryinstances:
                registry.update(_instance)
            for _instance in episodeinstances:
                registry.update(_instance)
            for _instance in seasoninstances:
                registry.update(_instance)
            for _instance in hostinstances:
                registry.update(_instance)
        if model_name == 'PodcastsModel':
            podcastinstances = instance.PodcastsModel.all()
            episodeinstances = instance.EpisodesModel.all()

            for _instance in podcastinstances:
                registry.update(_instance)
            for _instance in episodeinstances:
                registry.update(_instance)


@receiver(post_delete)
def delete_document(sender, **kwargs):
    """Update document on deleted records.
    Updates Book document from index if related `books.Publisher`
    (`publisher`), `books.Author` (`authors`), `books.Tag` (`tags`) fields
    have been removed from database.
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'podcast':
        # If it is `books.Publisher` that is being updated.
        if model_name == 'Episodesmodel':
            #[CategoriesModel, PodcastsModel, SeasonsModel, HostsModel]
            categoryinstances = instance.CategoriesModel.all()
            podcastinstances = instance.PodcastsModel.all()
            seasoninstances = instance.SeasonsModel.all()
            hostinstances = instance.HostsModel.all()
            for _instance in categoryinstances:
                registry.update(_instance)
            for _instance in podcastinstances:
                registry.update(_instance)
            for _instance in seasoninstances:
                registry.update(_instance)
            for _instance in hostinstances:
                registry.update(_instance)
        if model_name == 'HostsModel':
            podcastinstances = instance.PodcastsModel.all()
            episodeinstances = instance.EpisodesModel.all()
            for _instance in podcastinstances:
                registry.update(_instance)
            for _instance in episodeinstances:
                registry.update(_instance)
        if model_name == 'SeasonsModel':
            podcastinstances = instance.PodcastsModel.all()
            episodeinstances = instance.EpisodesModel.all()
            for _instance in podcastinstances:
                registry.update(_instance)
            for _instance in episodeinstances:
                registry.update(_instance)
        if model_name == 'PodcastsModel':
            categoryinstances = instance.CategoriesModel.all()
            episodeinstances = instance.EpisodesModel.all()
            seasoninstances = instance.SeasonsModel.all()
            hostinstances = instance.HostsModel.all()
            for _instance in categoryinstances:
                registry.update(_instance)
            for _instance in episodeinstances:
                registry.update(_instance)
            for _instance in seasoninstances:
                registry.update(_instance)
            for _instance in hostinstances:
                registry.update(_instance)
        if model_name == 'CategoriesModel':
            podcastinstances = instance.PodcastsModel.all()
            episodeinstances = instance.EpisodesModel.all()

            for _instance in podcastinstances:
                registry.update(_instance)
            for _instance in episodeinstances:
                registry.update(_instance)

    # if app_label == 'podcast':
    #     # If it is `books.Publisher` that is being updated.
    #     if model_name == 'ArtistsModel':
    #         instances = instance.ArtistsModel.all()
    #         for _instance in instances:
    #             registry.update(_instance)
    #     if model_name == 'AlbumsModel':
    #         instances = instance.AlbumsModel.all()
    #         for _instance in instances:
    #             registry.update(_instance)
    #     if model_name == 'GenresModel':
    #         instances = instance.GenresModel.all()
    #         for _instance in instances:
    #             registry.update(_instance)
    #     if model_name == 'TracksModel':
    #         instances = instance.TracksModel.all()
    #         for _instance in instances:
    #             registry.update(_instance)
