from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Brand, Tag
from .serializers import MovieSerializer
from rest_framework.decorators import api_view


# from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class MoviesListView(APIView):
    def get(self, request):
        search = request.GET.get("search")
        filter_by_tag = request.GET.get("filter_by_tag")
        print("in list view", search, filter_by_tag)
        qs = Movie.objects.all()
        if search is not None:
            qs = qs.filter(name__icontains=search)
        if filter_by_tag is not None:
            qs = qs.filter(tags__name__iexact=filter_by_tag)
        p = Paginator(qs, 2)
        page_number = request.GET.get("page")
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

        serializer = MovieSerializer(page_obj, many=True)

        return Response(
            {"movies": serializer.data, "pages": p.num_pages},
            status=status.HTTP_200_OK,
        )


def get_movie(slug):
    try:
        movie = Movie.objects.get(slug=slug)
        return movie
    except Movie.DoesNotExist:
        raise Http404


@api_view(http_method_names=["PUT"])
def increase_movie_downloads(request, slug):
    movie = get_movie(slug)
    movie.downloads += 1
    movie.save()
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["PUT"])
def increase_movie_likes(request, slug):
    movie = get_movie(slug)
    movie.likes += 1
    movie.save()
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["PUT"])
def increase_movie_dislikes(request, slug):
    movie = get_movie(slug)
    movie.dislikes += 1
    movie.save()
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)
