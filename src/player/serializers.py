from dataclasses import field, fields
from datetime import datetime
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.core.mail import send_mail

from .models import *

class HostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostsModel
        fields = '__all__'

    def create(self, validated_data):
        artist = super().create(validated_data)
        try:
            SingleSeason = SeasonsModel(
                season_name="Singles",
                season_status=validated_data['host_status'],
                season_releaseDate=datetime.now(),
                season_description=f"Contains all single episodes of the {validated_data['host_name']}!",
                season_coverImage=validated_data['host_profileImage'],
                encoder_FUI=validated_data['encoder_FUI']
            )
            SingleSeason.save()
            SingleSeason.host_id.add(artist)
        except BaseException as e:
            Subject = "Data Consistancy Problem"
            Email_Body = f"Error: {e}\n\nIssue: Singles season is not created for the host: {validated_data['host_name']}."
            Sender = 'kinideas.tech@gmail.com'
            Receiver = 'hailat.alx@gmail.com'

            send_mail(Subject, Email_Body, Sender, [Receiver], fail_silently=False,)
        return artist

class SeasonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeasonsModel
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):

     class Meta:
        model = CategoriesModel
        fields = '__all__'

class EpisodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = EpisodesModel
        fields = '__all__'

class PlayListsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PlayListsModel
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayListsModel.objects.all(),
                fields=['playlist_name', 'user_FUI']
            )
        ]

class PlayListsEpisodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayListEpisodesModel
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PlayListEpisodesModel.objects.all(),
                fields=['playlist_id', 'episode_id']
            )
        ]

class FavouritesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FavouritesModel
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=FavouritesModel.objects.all(),
                fields=['episode_id', 'user_FUI']
            )
        ]

class PurchasedEpisodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchasedEpisodesModel
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PurchasedEpisodesModel.objects.all(),
                fields=['episode_id', 'user_FUI']
            )
        ]

class PurchasedSeasonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchasedSeasonsModel
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=PurchasedSeasonsModel.objects.all(),
                fields=['season_id', 'user_FUI']
            )
        ]