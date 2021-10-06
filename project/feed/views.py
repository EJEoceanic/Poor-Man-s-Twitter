from django.shortcuts import render
from django.http import JsonResponse
from .models import Tweet
from rest_framework.viewsets import ModelViewSet
from .serializers import TweetSerializer


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

