from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article, UserFavouriteArticle

class TestAccess(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_views_access_authenticated_user(self):
        response = self.client.get(reverse('blog:favourites'))
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(reverse('blog:pub'))
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(reverse('blog:create'))
        self.assertEqual(response.status_code, 302)

        self.client.login(username='testuser', password='testpassword')
        
        response = self.client.get(reverse('blog:favourites'))
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get(reverse('blog:pub'))
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get(reverse('blog:create'))
        self.assertEqual(response.status_code, 200)

    def test_connected_user_cannot_register(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('blog:signup'))
        self.assertEqual(response.status_code, 302)

    def test_user_cannot_favorite_twice(self):
        self.client.login(username='testuser', password='testpassword')
        article = Article.objects.create(title='Test Article', author=self.user, synopsis="Test synopsis", content='Lorem ipsum')

        # Test qu'un utilisateur ne peut pas mettre deux fois le même article en favori
        response = self.client.post(reverse('blog:addToFavourite', kwargs={'pk': article.id}))
        response = self.client.post(reverse('blog:addToFavourite', kwargs={'pk': article.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(UserFavouriteArticle.objects.filter(user=self.user, article=article).count(), 1)

