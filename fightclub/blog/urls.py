from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "blog"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("articles", views.ArticlesView.as_view(), name="articles"),
    path("login", views.LoginView.as_view(), name="login"),
    path("register", views.SignupView.as_view(), name="signup"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("publications", views.PubView.as_view(), name="pub"),
    path("article/<int:pk>", views.ArticleDetailView.as_view(), name="article"),
    path("favourites", views.FavouriteView.as_view(), name="favourites"),
    path("create", views.CreateArticleView.as_view(), name="create"),
    path("addToFavourite/<int:pk>", views.AddToFavourites.as_view(), name="addToFavourite")
]
