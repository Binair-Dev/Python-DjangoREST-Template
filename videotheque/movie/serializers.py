from rest_framework import serializers
from .models import Movie, Director

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'first_name', 'last_name', 'nationality'] #OR '__all__'

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director_id = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Director.objects.all(),
        write_only=True,
        source='director') #Pour le post, envoyer l'id des réalisateurs
    
    director = serializers.HyperlinkedIdentityField(
        many=True,
        read_only=True,
        view_name='director-detail',
    )
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_date', 'director_id', 'identification_number', 'director'] #OR '__all__'
        #extra_kwargs = {'director': {'view_name': 'director-detail', 'lookup_field': 'pk', 'read_only': True}} #Alternative

#Manuellement: 
# class DirectorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     first_name = serializers.CharField(max_length=100)
#     last_name = serializers.CharField(max_length=100)
#     nationality = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         return Director.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.nationality = validated_data.get('nationality', instance.nationality)
#         instance.save()
#         return instance

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200)
#     release_date = serializers.DateField()
#     director = serializers.PrimaryKeyRelatedField(many=True, queryset=Director.objects.all())
#     identification_number = serializers.IntegerField()

#     def create(self, validated_data):
#         director = validated_data.pop('director')
#         movie = Movie.objects.create(**validated_data)
#         movie.director.set(director)
#         return movie
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.release_date = validated_data.get('release_date', instance.release_date)
#         instance.identification_number = validated_data.get('identification_number', instance.identification_number)
#         instance.save()

#         if 'director' in validated_data:
#             instance.director.set(validated_data['director']) # OR instance.director.set(validated_data.get('director'))
            

#         return instance