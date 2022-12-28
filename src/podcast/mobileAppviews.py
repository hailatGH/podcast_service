from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import *
from .serializers import *

# Standard Results Set Pagination 
class CategoryPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'

# Class based model viewsets for the Mobile App
class HostsMobileViewSet(viewsets.ModelViewSet):

    queryset = HostsModel.objects.all()
    serializer_class = HostsSerializer
    pagination_class = StandardResultsSetPagination

class CategoriesMobileViewSet(viewsets.ModelViewSet):
    
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = CategoryPagination

    def create(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def retrieve(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def update(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def partial_update(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def destroy(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def list(self, request, *args, **kwargs):
        category = self.queryset.filter(category_status=True).order_by('-created_at').values('id','category_name','category_coverImage')
        page = self.paginate_queryset(category)
        if page is not None:
            for category_count in range(len(page)):
                podcasts = PodcastsModel.objects.filter(podcast_status=True, category_id=page[category_count]['id'])
                if podcasts.exists():
                    page[category_count]['podcasts'] = []
                    podcasts = podcasts.values('id', 'podcast_name', 'podcast_description', 'podcast_coverImage', 'host', 'category', 'encoder_FUI')
                    for podcast_count in range(len(podcasts)):
                        podcast = {}
                        for val in ['id', 'podcast_name', 'podcast_description', 'podcast_coverImage', 'encoder_FUI', 'category', 'host']:
                            podcast[val] = podcasts[podcast_count][val]
                        podcast['host_name'] = HostsModel.objects.filter(host_status=True, id=podcasts[podcast_count]['host']).values('host_name')[0]['host_name']
                        podcast['numberOfSeasons'] = SeasonsModel.objects.filter(season_status=True, podcast=podcasts[podcast_count]['id']).count()
                        podcast['numberOfEpisodes'] = EpisodesModel.objects.filter(episode_status=True, podcast=podcasts[podcast_count]['id']).count()
                        page[category_count]['podcasts'].append(podcast)
        return Response(page)

class PodcastsMobileViewSet(viewsets.ModelViewSet):

    queryset = PodcastsModel.objects.all()
    serializer_class = PodcastsSerializer
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def retrieve(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def update(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def partial_update(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def destroy(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def list(self, request, *args, **kwargs):
        podcasts = self.queryset.filter(podcast_status=True).order_by('-created_at').values('id', 'podcast_name', 'podcast_description', 'podcast_coverImage', 'host', 'category', 'encoder_FUI')
        page = self.paginate_queryset(podcasts)
        if page is not None:
            for podcast_count in range(len(page)):
                page[podcast_count]['host_name'] = HostsModel.objects.filter(host_status=True, id=page[podcast_count]['host']).values('host_name')[0]['host_name']
                page[podcast_count]['numberOfSeasons'] = SeasonsModel.objects.filter(season_status=True, podcast=page[podcast_count]['id']).count()
                page[podcast_count]['numberOfEpisodes'] = EpisodesModel.objects.filter(episode_status=True, podcast=page[podcast_count]['id']).count()
                # podcasts = PodcastsModel.objects.filter(podcast_status=True, category_id=page[category_count]['id'])
            #     if podcasts.exists():
            #         page[category_count]['podcasts'] = []
            #         podcasts = podcasts.values('id', 'podcast_name', 'podcast_description', 'podcast_coverImage', 'host', 'encoder_FUI')
            #         for podcast_count in range(len(podcasts)):
            #             podcast = {}
            #             for val in ['id', 'podcast_name', 'podcast_description', 'podcast_coverImage', 'encoder_FUI', 'host']:
            #                 podcast[val] = podcasts[podcast_count][val]
            #             podcast['host_name'] = HostsModel.objects.filter(host_status=True, id=podcasts[podcast_count]['host']).values('host_name')[0]['host_name']
            #             podcast['numberOfSeasons'] = SeasonsModel.objects.filter(season_status=True, podcast=podcasts[podcast_count]['id']).count()
            #             podcast['numberOfEpisodes'] = EpisodesModel.objects.filter(episode_status=True, podcast=podcasts[podcast_count]['id']).count()
            #             page[category_count]['podcasts'].append(podcast)
        return Response(page)

class SeasonsMobileViewSet(viewsets.ModelViewSet):

    queryset = SeasonsModel.objects.all()
    serializer_class = SeasonsSerializer
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def retrieve(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def update(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def partial_update(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def destroy(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def list(self, request, *args, **kwargs):
        podcastId = request.query_params['podcastId']
        seasons = self.queryset.filter(season_status=True, podcast=podcastId).order_by('-created_at').values('id', 'season_name', 'season_coverImage', 'podcast')
        page = self.paginate_queryset(seasons)
        if page is not None:
            for season_count in range(len(page)):
                page[season_count]['numberOfEpisodes'] = EpisodesModel.objects.filter(episode_status=True, podcast=page[season_count]['podcast']).count()
                # podcasts = PodcastsModel.objects.filter(podcast_status=True, category_id=page[category_count]['id'])
            #     if podcasts.exists():
            #         page[category_count]['podcasts'] = []
            #         podcasts = podcasts.values('id', 'podcast_name', 'podcast_description', 'podcast_coverImage', 'host', 'encoder_FUI')
            #         for podcast_count in range(len(podcasts)):
            #             podcast = {}
            #             for val in ['id', 'podcast_name', 'podcast_description', 'podcast_coverImage', 'encoder_FUI', 'host']:
            #                 podcast[val] = podcasts[podcast_count][val]
            #             podcast['host_name'] = HostsModel.objects.filter(host_status=True, id=podcasts[podcast_count]['host']).values('host_name')[0]['host_name']
            #             podcast['numberOfSeasons'] = SeasonsModel.objects.filter(season_status=True, podcast=podcasts[podcast_count]['id']).count()
            #             podcast['numberOfEpisodes'] = EpisodesModel.objects.filter(episode_status=True, podcast=podcasts[podcast_count]['id']).count()
            #             page[category_count]['podcasts'].append(podcast)
        return Response(page)

class EpisodesMobileViewSet(viewsets.ModelViewSet):
    
    queryset = EpisodesModel.objects.all()
    serializer_class = EpisodesSerializer
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def retrieve(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def update(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def partial_update(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def destroy(self, request, *args, **kwargs):
        return Response("Not Allowed")

    def list(self, request, *args, **kwargs):
        seasonId = request.query_params['seasonId']
        episodes = self.queryset.filter(episode_status=True, season=seasonId).order_by('-created_at').values('id', 'episode_name', 'episode_coverImage', 'episode_audioFile', 'host', 'podcast', 'category', 'encoder_FUI')
        page = self.paginate_queryset(episodes)
        if page is not None:
            for episode_count in range(len(page)):
                page[episode_count]['host_name'] = HostsModel.objects.filter(host_status=True, id=page[episode_count]['host']).values('host_name')[0]['host_name']
                # page[episode_count]['numberOfEpisodes'] = EpisodesModel.objects.filter(episode_status=True, podcast=page[season_count]['podcast']).count()
                # podcasts = PodcastsModel.objects.filter(podcast_status=True, category_id=page[category_count]['id'])
            #     if podcasts.exists():
            #         page[category_count]['podcasts'] = []
            #         podcasts = podcasts.values('id', 'podcast_name', 'podcast_description', 'podcast_coverImage', 'host', 'encoder_FUI')
            #         for podcast_count in range(len(podcasts)):
            #             podcast = {}
            #             for val in ['id', 'podcast_name', 'podcast_description', 'podcast_coverImage', 'encoder_FUI', 'host']:
            #                 podcast[val] = podcasts[podcast_count][val]
            #             podcast['host_name'] = HostsModel.objects.filter(host_status=True, id=podcasts[podcast_count]['host']).values('host_name')[0]['host_name']
            #             podcast['numberOfSeasons'] = SeasonsModel.objects.filter(season_status=True, podcast=podcasts[podcast_count]['id']).count()
            #             podcast['numberOfEpisodes'] = EpisodesModel.objects.filter(episode_status=True, podcast=podcasts[podcast_count]['id']).count()
            #             page[category_count]['podcasts'].append(podcast)
        return Response(page)

# class PodcastsMobileViewSet(viewsets.ModelViewSet):

#     queryset = PodcastsModel.objects.all()
#     serializer_class = PodcastsSerializer
#     pagination_class = StandardResultsSetPagination

#     def create(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def retrieve(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def partial_update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def destroy(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def list(self, request, *args, **kwargs):
#         Podcasts = self.queryset.filter(host_status=True).order_by('-created_at').values('id','host_name','host_profileImage')
#         page = self.paginate_queryset(Podcasts)
#         if page is not None:
#             for host_count in range(len(page)):
#                 seasons = SeasonsModel.objects.filter(season_status=True, host_id=page[host_count]['id'])
#                 page[host_count]['noOfSeasons'] = seasons.count() - 1
#         return Response(page)

# class SeasonByHostIdViewSet(viewsets.ModelViewSet):

#     queryset = SeasonsModel.objects.all()
#     serializer_class = SeasonsSerializer
#     pagination_class = StandardResultsSetPagination

#     def create(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def retrieve(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def partial_update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def destroy(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def list(self, request, *args, **kwargs):
#         userId = request.query_params['userId']
#         hostId = request.query_params['hostId']
#         seasons = self.queryset.filter(season_status=True, host_id=hostId).order_by('-created_at').values('id','season_name','season_coverImage','season_description','season_price','host_id')
#         page = self.paginate_queryset(seasons)
#         if page is not None:
#             for season_count in range(len(page)):
#                 Podcasts = PodcastsModel.objects.filter(id=page[season_count]['host_id'])
#                 host_name = ""
#                 if Podcasts.count() > 1:
#                     for host_count in range(len(Podcasts)):    
#                         host_name = host_name + ", " + Podcasts.values('host_name')[host_count]['host_name']
#                 else:
#                     host_name = Podcasts.values('host_name')[0]['host_name']
#                 page[season_count]['host_name'] = host_name
#                 page[season_count]['is_purchasedByUser'] = PurchasedSeasonsModel.objects.filter(season_id=page[season_count]['id'], user_FUI=userId).exists()
#         return Response(page)

# class SeasonsMobileViewSet(viewsets.ModelViewSet):

#     queryset = SeasonsModel.objects.all()
#     serializer_class = SeasonsSerializer
#     pagination_class = StandardResultsSetPagination

#     def create(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def retrieve(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def partial_update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def destroy(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def list(self, request, *args, **kwargs):
#         userId = request.query_params['userId']
#         seasons = self.queryset.filter(season_status=True).order_by('-created_at').values('id','season_name','season_coverImage','season_description','season_price','host_id')
#         page = self.paginate_queryset(seasons)
#         if page is not None:
#             for season_count in range(len(page)):
#                 Podcasts = PodcastsModel.objects.filter(id=page[season_count]['host_id'])
#                 page[season_count]['host_name'] = Podcasts.values('host_name')[0]['host_name']
#                 page[season_count]['is_purchasedByUser'] = PurchasedSeasonsModel.objects.filter(season_id=page[season_count]['id'], user_FUI=userId).exists()
#         return Response(page)

# class EpisodesBySeasonIdViewSet(viewsets.ModelViewSet):

#     queryset = EpisodesModel.objects.all()
#     serializer_class = EpisodesSerializer
#     pagination_class = StandardResultsSetPagination

#     def create(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def retrieve(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def partial_update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def destroy(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def list(self, request, *args, **kwargs):
#         userId = request.query_params['userId']
#         seasonId = request.query_params['seasonId']
#         episodes = self.queryset.filter(episode_status=True, season_id=seasonId).order_by('-created_at').values('id','episode_name','episode_description','episode_coverImage','episode_audioFile','episode_price','host_id','season_id','category_id')
#         page = self.paginate_queryset(episodes)
#         if page is not None:
#             for episode_count in range(len(page)):
#                 Podcasts = PodcastsModel.objects.filter(id=page[episode_count]['host_id'])
#                 page[episode_count]['host_name'] = Podcasts.values('host_name')[0]['host_name']
#                 page[episode_count]['is_purchasedByUser'] = PurchasedEpisodesModel.objects.filter(episode_id=page[episode_count]['id'], user_FUI=userId).exists()
#         return Response(page)

# class CategoriesMobileViewSet(viewsets.ModelViewSet):

#     queryset = CategoriesModel.objects.all()
#     serializer_class = CategoriesSerializer
#     pagination_class = StandardResultsSetPagination

#     def create(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def retrieve(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def partial_update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def destroy(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def list(self, request, *args, **kwargs):
#         categories = self.queryset.filter(category_status=True).order_by('-created_at').values('id','category_name','category_description','category_coverImage')
#         page = self.paginate_queryset(categories)
#         return Response(page)

# class EpisodesByCategoryIdViewSet(viewsets.ModelViewSet):

#     queryset = EpisodesModel.objects.all()
#     serializer_class = EpisodesSerializer
#     pagination_class = StandardResultsSetPagination

#     def create(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def retrieve(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def partial_update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def destroy(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def list(self, request, *args, **kwargs):
#         userId = request.query_params['userId']
#         categoryId = request.query_params['categoryId']
#         episodes = self.queryset.filter(episode_status=True, category_id=categoryId).order_by('-created_at').values('id','episode_name','episode_description','episode_coverImage','episode_audioFile','episode_price','host_id','season_id','category_id')
#         page = self.paginate_queryset(episodes)
#         if page is not None:
#             for episode_count in range(len(page)):
#                 Podcasts = PodcastsModel.objects.filter(id=page[episode_count]['host_id'])
#                 page[episode_count]['host_name'] = Podcasts.values('host_name')[0]['host_name']
#                 page[episode_count]['is_purchasedByUser'] = PurchasedEpisodesModel.objects.filter(episode_id=page[episode_count]['id'], user_FUI=userId).exists()
#         return Response(page)

# class EpisodesMobileViewSet(viewsets.ModelViewSet):

#     queryset = EpisodesModel.objects.all()
#     serializer_class = EpisodesSerializer
#     pagination_class = StandardResultsSetPagination

#     def create(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def retrieve(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def partial_update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def destroy(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def list(self, request, *args, **kwargs):
#         userId = request.query_params['userId']
#         episodes = self.queryset.filter(episode_status=True).order_by('-created_at').values('id','episode_name','episode_description','episode_coverImage','episode_audioFile','episode_price','host_id','season_id','category_id')
#         page = self.paginate_queryset(episodes)
#         if page is not None:
#             for episode_count in range(len(page)):
#                 Podcasts = PodcastsModel.objects.filter(id=page[episode_count]['host_id'])
#                 page[episode_count]['host_name'] = Podcasts.values('host_name')[0]['host_name']
#                 page[episode_count]['is_purchasedByUser'] = PurchasedEpisodesModel.objects.filter(episode_id=page[episode_count]['id'], user_FUI=userId).exists()
#         return Response(page)

# class FavouritesByUserIdViewSet(viewsets.ModelViewSet):

#     queryset = FavouritesModel.objects.all()
#     serializer_class = FavouritesSerializer
#     pagination_class = StandardResultsSetPagination

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def partial_update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

#     def list(self, request, *args, **kwargs):
#         userId = request.query_params['userId']
#         favouries = self.queryset.filter(user_FUI=userId).order_by('-created_at').values('id','episode_id')
#         page = self.paginate_queryset(favouries)
#         if page is not None:
#             for fav_count in range(len(page)):
#                 page[fav_count]['fav_id'] = page[fav_count]['id']
#                 episodes = EpisodesModel.objects.filter(episode_status=True, id=page[fav_count]['episode_id']).order_by('-created_at').values('id','episode_name','episode_description','episode_coverImage','episode_audioFile','episode_price','host_id','season_id','category_id')
#                 for val in ['id','episode_name','episode_description','episode_coverImage','episode_audioFile','episode_price','host_id','season_id','category_id']:
#                     page[fav_count][val] = episodes[0][val]
#                 Podcasts = PodcastsModel.objects.filter(id=page[fav_count]['host_id'])
#                 page[fav_count]['host_name'] = Podcasts.values('host_name')[0]['host_name']
#                 page[fav_count]['is_purchasedByUser'] = PurchasedEpisodesModel.objects.filter(episode_id=page[fav_count]['id'], user_FUI=userId).exists()
#         return Response(page)

# class PlayListsByUserIdViewSet(viewsets.ModelViewSet):
    
#     queryset = PlayListsModel.objects.all()
#     serializer_class = PlayListsSerializer
#     pagination_class = StandardResultsSetPagination

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)

#     def partial_update(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)

#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

#     def list(self, request, *args, **kwargs):
#         userId = request.query_params['userId']
#         playlist = self.queryset.filter(user_FUI=userId).order_by('-created_at').values('id','playlist_name','user_FUI')
#         page = self.paginate_queryset(playlist)
#         return Response(page)

# class PlayListEpisodesByPlaylistIdViewSet(viewsets.ModelViewSet):
    
#     queryset = PlayListEpisodesModel.objects.all()
#     serializer_class = PlayListsEpisodesSerializer
#     pagination_class = StandardResultsSetPagination

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     def retrieve(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def partial_update(self, request, *args, **kwargs):
#         return Response("Not Allowed")

#     def destroy(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

#     def list(self, request, *args, **kwargs):
#         userId = request.query_params['userId']
#         playlistId = request.query_params['playlistId']
#         playlistEpisodes = self.queryset.filter(playlist_id=playlistId).order_by('-created_at').values('id','playlist_id','episode_id')
#         page = self.paginate_queryset(playlistEpisodes)
#         if page is not None:
#             for episode_count in range(len(page)):
#                 page[episode_count]['playlist_episode_id'] = page[episode_count]['id']
#                 episodes = EpisodesModel.objects.filter(id=page[episode_count]['episode_id']).order_by('-created_at').values('id','episode_name','episode_description','episode_coverImage','episode_audioFile','episode_price','host_id','season_id','category_id')
#                 for val in ['id','episode_name','episode_description','episode_coverImage','episode_audioFile','episode_price','host_id','season_id','category_id']:
#                     page[episode_count][val] = episodes[0][val]
#                 Podcasts = PodcastsModel.objects.filter(id=page[episode_count]['host_id'])
#                 page[episode_count]['host_name'] = Podcasts.values('host_name')[0]['host_name']
#                 page[episode_count]['is_purchasedByUser'] = PurchasedEpisodesModel.objects.filter(episode_id=page[episode_count]['id'], user_FUI=userId).exists()
#         return Response(page)