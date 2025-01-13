from .models import Article
from rest_framework import serializers
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "first_name", "last_name")


class ArticleSerializer(serializers.ModelSerializer):
    # author = serializers.HyperlinkedRelatedField(view_name="author-detail", read_only=True)
    # author = serializers.CharField(source="author.username", read_only=True)
    author = serializers.SerializerMethodField("get_author")

    def get_author(self, obj):
        return {
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name,
        }

    class Meta:
        model = Article
        fields = "__all__"

    def validate_title(self, value):
        filter_list = ("python", "java")
        for word in filter_list:
            if word in value:
                raise serializers.ValidationError(f"forbiden world: {word}")
        return value
