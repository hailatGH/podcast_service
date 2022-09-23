from rest_framework.routers import DefaultRouter

from player.views import *
# from player.mobileAppviews import *

webApprouter = DefaultRouter(trailing_slash=False)
webApprouter.register(r'host', HostsWebViewSet, basename="host")
webApprouter.register(r'season', SeasonsWebViewSet, basename="season")
webApprouter.register(r'category', CategoriesWebViewSet, basename="category")
webApprouter.register(r'episode', EpisodesWebViewSet, basename="episode")
webApprouter.register(r'playlist', PlayListsWebViewSet, basename="playlist")
webApprouter.register(r'playlistepisode', PlayListEpisodesWebViewSet, basename="playlistepisode")
webApprouter.register(r'purchasedepisode', PurchasedEpisodesWebViewSet, basename="purchasedepisode")
webApprouter.register(r'purchasedseason', PurchasedSeasonsWebViewSet, basename="purchasedseason")

mobileApprouter = DefaultRouter(trailing_slash=False)
# mobileApprouter.register(r'artists', ArtistsMobileViewSet, basename="artists")
# mobileApprouter.register(r'albumsByArtistId', AlbumByArtistIdViewSet, basename="albumsByArtistId")
# mobileApprouter.register(r'albums', AlbumsMobileViewSet, basename="albums")
# mobileApprouter.register(r'tracksByAlbumId', TracksByAlbumIdViewSet, basename="tracksByAlbumId")
# mobileApprouter.register(r'genres', GenresMobileViewSet, basename="genres")
# mobileApprouter.register(r'tracksByGenreId', TracksByGenreIdViewSet, basename="tracksByGenreId")
# mobileApprouter.register(r'tracks', TracksMobileViewSet, basename="tracks")
# mobileApprouter.register(r'favTracks', FavouritesByUserIdViewSet, basename="favTracks")
# mobileApprouter.register(r'playlists', PlayListsByUserIdViewSet, basename="playlists")
# mobileApprouter.register(r'tracksByPlaylistId', PlayListTracksByPlaylistIdViewSet, basename="tracksByPlaylistId")