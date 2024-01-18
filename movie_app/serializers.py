from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields ='__all__'


class DirectorValidatorSerializer(serializers.Serializer):
    name = serializers.CharField()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieValidatorSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    duration = serializers.IntegerField(max_value=240)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'movie']


class ReviewValidatorSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(max_value=5)

