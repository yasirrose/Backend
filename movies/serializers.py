from rest_framework import serializers
from .models import Movie, Tag, Brand


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    brand = BrandSerializer()

    class Meta:
        model = Movie
        fields = "__all__"
