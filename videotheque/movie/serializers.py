from rest_framework import serializers
from movie.models import Director
from .models import Movie, Director

class DirectorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    nationality = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Director.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.save()
        return instance

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    release_date = serializers.DateField()
    director = serializers.PrimaryKeyRelatedField(many=True, queryset=Director.objects.all())
    identification_number = serializers.IntegerField()

    def create(self, validated_data):
        director = validated_data.pop('director')
        movie = Movie.objects.create(**validated_data)
        movie.director.set(director)
        return movie
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.identification_number = validated_data.get('identification_number', instance.identification_number)
        instance.save()

        if 'director' in validated_data:
            instance.director.set(validated_data.get('director'))

        return instance