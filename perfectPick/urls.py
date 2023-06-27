from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginForm, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logoutLink, name="logout"),
    path("", views.index, name="index"),
    path("movie/<int:movieID>", views.movieInfo, name="movieInfo"),
    path("search/<str:category>/<str:query>", views.search, name="search"),
    path("watchlist", views.watchlistItems, name="watchlistPage"),
    path("watchlistAdd/<int:movieId>/<int:removeOrAdd>", views.watchlistAdd, name="watchlistAdd"),
    path("like/<int:movieID>/<int:check>", views.like, name="like"),
    path("liked", views.liked, name="liked")
]