from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Author, Book

User = get_user_model()

class BookAPITest(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )

        # Authenticate the DRF test client
        self.client.force_authenticate(user=self.user)

        # Create an author and a sample book
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

    def test_list_books(self):
        """Test retrieving the list of books (anyone can read)"""
        # Allow unauthenticated access for list
        self.client.force_authenticate(user=None)  # remove authentication
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", [book["title"] for book in response.data])

    def test_create_book(self):
        """Test creating a book (authenticated users only)"""
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(reverse('book-create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")
