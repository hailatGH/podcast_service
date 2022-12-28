from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import *
from .serializers import *

# Standard Results Set Pagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

# Class based model viewsets for the Web App


class HostsWebViewSet(viewsets.ModelViewSet):

    queryset = HostsModel.objects.all()
    serializer_class = HostsSerializer
    pagination_class = StandardResultsSetPagination


class CategoriesWebViewSet(viewsets.ModelViewSet):

    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = StandardResultsSetPagination


class PodcastsWebViewSet(viewsets.ModelViewSet):

    queryset = PodcastsModel.objects.all()
    serializer_class = PodcastsSerializer
    pagination_class = StandardResultsSetPagination


class SeasonsWebViewSet(viewsets.ModelViewSet):

    queryset = SeasonsModel.objects.all()
    serializer_class = SeasonsSerializer
    pagination_class = StandardResultsSetPagination


class EpisodesWebViewSet(viewsets.ModelViewSet):

    queryset = EpisodesModel.objects.all()
    serializer_class = EpisodesSerializer
    pagination_class = StandardResultsSetPagination

# class PlayListsWebViewSet(viewsets.ModelViewSet):

#     queryset = PlayListsModel.objects.all()
#     serializer_class = PlayListsSerializer
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

# class PlayListEpisodesWebViewSet(viewsets.ModelViewSet):

#     queryset = PlayListEpisodesModel.objects.all()
#     serializer_class = PlayListsEpisodesSerializer
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

# class PurchasedEpisodesWebViewSet(viewsets.ModelViewSet):

#     queryset = PurchasedEpisodesModel.objects.all()
#     serializer_class  = PurchasedEpisodesSerializer

# class PurchasedSeasonsWebViewSet(viewsets.ModelViewSet):

#     queryset = PurchasedSeasonsModel.objects.all()
#     serializer_class = PurchasedSeasonsSerializer
#     pagination_class = StandardResultsSetPagination
