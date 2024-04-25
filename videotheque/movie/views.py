from .models import Director, Movie
from .serializers import DirectorSerializer, MovieSerializer
from rest_framework import generics as generic

#Create your views here.
class DirectorList(generic.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetail(generic.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieList(generic.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generic.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

#API VIEW Template
# class DirectorList(APIView):
#     def get(self, request):
#         # if not request.user.is_authenticated:
#         #     return Response(status=status.HTTP_401_UNAUTHORIZED) #Si on veut protéger le get des utilisateurs non authentifiés
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = DirectorSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# class DirectorDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly] #Si on veut protéger le requetes des utilisateurs non authentifiés
#     def get_object(self, id):
#         try:
#             return Director.objects.get(id=id)
#         except Director.DoesNotExist:
#             raise NotFound(detail="Le réalisateur avec l'id {} n'existe pas".format(id))
    
#     def get(self, request, id):
#         director = self.get_object(id)
#         serializer = DirectorSerializer(director, context={'request': request})
#         return Response(serializer.data)

#     def put(self, request, id):
#         director = self.get_object(id)
#         serializer = DirectorSerializer(director, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, id):
#         director = self.get_object(id)
#         serializer = DirectorSerializer(director, data=request.data, partial=True, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         director = self.get_object(id)
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class MovieList(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MovieSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# class MovieDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly] #Si on veut protéger le requetes des utilisateurs non authentifiés
#     def get_object(self, id):
#         try:
#             return Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             raise NotFound(detail="Le film avec l'id {} n'existe pas".format(id))
    
#     def get(self, request, id):
#         movie = self.get_object(id)
#         serializer = MovieSerializer(movie, context={'request': request})
#         return Response(serializer.data)

#     def put(self, request, id):
#         movie = self.get_object(id)
#         serializer = MovieSerializer(movie, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, id):
#         movie = self.get_object(id)
#         serializer = MovieSerializer(movie, data=request.data, partial=True, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         movie = self.get_object(id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

#BASIC Template
# @csrf_exempt 
# def director_list_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = DirectorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    
# @csrf_exempt
# def director_detail_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = DirectorSerializer(director)
#         return JsonResponse(serializer.data)

#     if request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = DirectorSerializer(director, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
        
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         data = JSONParser().parse(request)
#         serializer = DirectorSerializer(director, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
        
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         director.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
# @csrf_exempt 
# def movie_list_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = MovieSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    
# @csrf_exempt
# def movie_details_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return JsonResponse(serializer.data)

#     if request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = MovieSerializer(movie, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PATCH':
#         data = JSONParser().parse(request)
#         serializer = MovieSerializer(movie, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
        
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         movie.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)