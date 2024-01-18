# views.py

from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Director, Movie, Review
from .serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer)


class DirectorsListAPIView(ListAPIView, CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination


class DirectorDetailAPIView(RetrieveDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination


class MovieDetailAPIView(RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination


class ReviewDetailAPIView(RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'




# @api_view(['GET', 'POST'])
# def director_list(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = DirectorValidatorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             Director.objects.create(name=serializer.validate['name'])
#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail(request, id):
#     director = get_object_or_404(Director, id=id)
#     if request.method == 'GET':
#         serializer = DirectorSerializer(director)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = DirectorValidatorSerializer(data=request.data)
#         if serializer.is_valid():
#             director.name = serializer.validated_data['name']
#             serializer.save()
#             return Response(serializer.validated_data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieValidatorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             Movie.objects.create(
#                 title=serializer.validated_data['title'],
#                 description=serializer.validated_data['description'],
#                 duration=serializer.validated_data['duration']
#             )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, id):
#     movie = get_object_or_404(Movie, id=id)
#     if request.method == 'GET':
#         serializer = MovieValidatorSerializer(data=request.data)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             movie.title = serializer.validated_data['title']
#             movie.description = serializer.validated_data['description']
#             movie.duration = serializer.validated_data['duration']
#             serializer.save()
#             return Response(serializer.validated_data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def review_list(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             Review.objects.create(
#                 text=serializer.validated_data['text'],
#                 stars=serializer.validated_data['stars']
#             )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail(request, id):
#     review = get_object_or_404(Review, id=id)
#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ReviewValidatorSerializer(data=request.data)
#         if serializer.is_valid():
#             review.text = serializer.validated_data['text']
#             review.stars = serializer.validated_data['stars']
#             serializer.save()
#             return Response(serializer.validated_data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
