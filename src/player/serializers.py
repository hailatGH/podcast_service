from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *

class HostsSerializer(serializers.ModelSerializer):

     class Meta:
        model = HostsModel
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):

     class Meta:
        model = CategoriesModel
        fields = '__all__'

class PodcastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastsModel
        fields = '__all__'

class SeasonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeasonsModel
        fields = '__all__'

class EpisodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = EpisodesModel
        fields = '__all__'

# class PlayListsSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = PlayListsModel
#         fields = '__all__'

#         validators = [
#             UniqueTogetherValidator(
#                 queryset=PlayListsModel.objects.all(),
#                 fields=['playlist_name', 'user_FUI']
#             )
#         ]

# class PlayListsEpisodesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = PlayListEpisodesModel
#         fields = '__all__'

#         validators = [
#             UniqueTogetherValidator(
#                 queryset=PlayListEpisodesModel.objects.all(),
#                 fields=['playlist_id', 'episode_id']
#             )
#         ]

# class FavouritesSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = FavouritesModel
#         fields = '__all__'

#         validators = [
#             UniqueTogetherValidator(
#                 queryset=FavouritesModel.objects.all(),
#                 fields=['episode_id', 'user_FUI']
#             )
#         ]

# class PurchasedEpisodesSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = PurchasedEpisodesModel
#         fields = '__all__'

#         validators = [
#             UniqueTogetherValidator(
#                 queryset=PurchasedEpisodesModel.objects.all(),
#                 fields=['episode_id', 'user_FUI']
#             )
#         ]

# class PurchasedSeasonsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = PurchasedSeasonsModel
#         fields = '__all__'

#         validators = [
#             UniqueTogetherValidator(
#                 queryset=PurchasedSeasonsModel.objects.all(),
#                 fields=['season_id', 'user_FUI']
#             )
#         ]