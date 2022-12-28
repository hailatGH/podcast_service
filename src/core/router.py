from rest_framework.routers import DefaultRouter

from podcast.webAppviews import *
from podcast.mobileAppviews import *

webApprouter = DefaultRouter(trailing_slash=False)
webApprouter.register(r'host', HostsWebViewSet, basename="host")
webApprouter.register(r'category', CategoriesWebViewSet, basename="category")
webApprouter.register(r'podcast', PodcastsWebViewSet, basename="podcast")
webApprouter.register(r'season', SeasonsWebViewSet, basename="season")
webApprouter.register(r'episode', EpisodesWebViewSet, basename="episode")
# webApprouter.register(r'playlist', PlayListsWebViewSet, basename="playlist")
# webApprouter.register(r'playlistepisode', PlayListEpisodesWebViewSet, basename="playlistepisode")
# webApprouter.register(r'purchasedepisode', PurchasedEpisodesWebViewSet, basename="purchasedepisode")
# webApprouter.register(r'purchasedseason', PurchasedSeasonsWebViewSet, basename="purchasedseason")

mobileApprouter = DefaultRouter(trailing_slash=False)
mobileApprouter.register(r'hosts', HostsMobileViewSet, basename="hosts")
mobileApprouter.register(
    r'categories', CategoriesMobileViewSet, basename="categories")
mobileApprouter.register(
    r'podcasts', PodcastsMobileViewSet, basename="podcasts")
mobileApprouter.register(r'seasons', SeasonsMobileViewSet, basename="seasons")
mobileApprouter.register(
    r'episodes', EpisodesMobileViewSet, basename="episodes")
# mobileApprouter.register(r'categories', CategoriesMobileViewSet, basename="categories")
# mobileApprouter.register(r'episodesByCategoryId', EpisodesByCategoryIdViewSet, basename="episodesByCategoryId")
# mobileApprouter.register(r'episodes', EpisodesMobileViewSet, basename="episodes")
# mobileApprouter.register(r'favEpisodes', FavouritesByUserIdViewSet, basename="favEpisodes")
# mobileApprouter.register(r'playlists', PlayListsByUserIdViewSet, basename="playlists")
# mobileApprouter.register(r'episodesByPlaylistId', PlayListEpisodesByPlaylistIdViewSet, basename="episodesByPlaylistId")
