from . import serializers, models
from rest_framework.generics import \
    (ListCreateAPIView,
     RetrieveUpdateDestroyAPIView)
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model


# Category classes
class CategoryList(ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


# News classes
class NewsList(ListCreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


class NewsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer


# Commit classes
class CommitList(ListCreateAPIView):
    queryset = models.Commit.objects.all()
    serializer_class = serializers.CommitSerializer


class CommitDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = models.Commit.objects.all()
    serializer_class = serializers.CommitSerializer


# User classes
class UserList(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
