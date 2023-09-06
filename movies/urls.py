from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.MoviesListView.as_view(), name="all-movies"),
    path("likes/<str:slug>", views.increase_movie_likes),
    path("dislikes/<str:slug>", views.increase_movie_dislikes),
    path("downloads/<str:slug>", views.increase_movie_downloads),
]
