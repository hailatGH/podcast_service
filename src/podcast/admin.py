from django.contrib import admin

from .models import *

admin.site.register(PodcastsModel)
admin.site.register(SeasonsModel)
admin.site.register(CategoriesModel)
admin.site.register(EpisodesModel)
# admin.site.register(PlayListsModel)
# admin.site.register(PlayListEpisodesModel)
# admin.site.register(FavouritesModel)
# admin.site.register(PurchasedEpisodesModel)
# admin.site.register(PurchasedSeasonsModel)