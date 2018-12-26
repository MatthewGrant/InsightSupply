from django.shortcuts import render
from rest_framework import generics
# from rest_framework.permissions import IsAdminUser

from notes import models, serializers


# TODO: Permission based views for anything but GET request
        # diffrent serializers for GET vs POST

class ListInsights(generics.ListCreateAPIView):
    serializer_class = serializers.InsightSerializer

    def get_queryset(self):
        queryset = models.Insight.objects.all().order_by('pk')
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__name=category).order_by('pk')
        return queryset


class DetailInsight(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Insight.objects.all()
    serializer_class = serializers.InsightSerializer


class ListCategories(generics.ListCreateAPIView):
    queryset = models.Category.objects.filter(active=True)
    serializer_class = serializers.CategorySerializer
