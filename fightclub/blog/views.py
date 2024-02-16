from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, login
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


from .forms import CreateArticleForm, UserFavouriteArticleForm
from .models import Article, UserFavouriteArticle


class ArticlesView(generic.ListView):
    model = Article
    template_name = "blog/article_list.html"


class HomeView(generic.base.RedirectView):
    pattern_name = "blog:articles"


class PubView(LoginRequiredMixin, generic.ListView):
    model = Article
    template_name = "blog/pub_list.html"
    login_url = "blog:login"

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = "blog/article_detail.html"


class FavouriteView(LoginRequiredMixin, generic.ListView):
    model = UserFavouriteArticle
    context_object_name = "articles"
    template_name = "blog/favourite_list.html"
    login_url = "blog:login"

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(user=self.request.user)


class LoginView(generic.edit.FormView):
    template_name = "blog/login.html"
    form_class = AuthenticationForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:home")


class SignupView(generic.edit.CreateView):
    model = User
    template_name = "blog/signup.html"
    form_class = UserCreationForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('blog:home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        res = super().form_valid(form)
        login(self.request, form.instance)
        return res

    def get_success_url(self):
        return reverse("blog:home")

class LogoutView(generic.base.RedirectView):
    pattern_name = "blog:home"

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return super().get(request, *args, **kwargs)


class CreateArticleView(LoginRequiredMixin, generic.edit.CreateView):
    model = Article
    template_name = "blog/create_article.html"
    form_class = CreateArticleForm
    login_url = "blog:login"

    def get_success_url(self):
        return reverse("blog:pub")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddToFavourites(LoginRequiredMixin, generic.edit.CreateView):
    model = UserFavouriteArticle
    form_class = UserFavouriteArticleForm 

    def form_valid(self, form):
        user = self.request.user
        article = Article.objects.get(pk=self.kwargs['pk'])
        if UserFavouriteArticle.objects.filter(user=user, article=article).exists():
            messages.info(self.request, "The article is already in your favourites")
            return redirect('blog:article', pk=article.id)
        form.instance.user = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:article', kwargs={'pk': self.kwargs['pk']})
