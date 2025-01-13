from .models import Article
from rest_framework import permissions
from .serializers import AuthorSerializer
from .serializers import ArticleSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ["status", "author__username"]
    search_fields = ["title", "content"]
    ordering_flelds = ["-published_at", "status"]
    ordering = ["-published_at"]


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class AuthorList(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]


class AuthorDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]
