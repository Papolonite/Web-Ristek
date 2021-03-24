from datetime import datetime, timezone
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blog, Blog_user, Comment


class DatabaseTest(TestCase):  # Testing for database
    def setUp(self):
        test_user_init = User.objects.create_user(username='People123', password='12345')
        test_user = User.objects.get(username='People123')
        blog_user = Blog_user.objects.create(user=test_user, birthday=datetime(2010,1,1))
        blog = Blog.objects.create(user_blog=blog_user, title="Hello World", blog_content="Hello World", like=0)
        comment = Comment.objects.create(user_comment=blog_user, on_blog=blog, comment_content="Hello")

    # Checking whether data is created correctly or not in database
    def test_check_amount_of_user(self):
        self.assertEqual(len(User.objects.all()),1)

    def test_check_amount_of_blog_user(self):
        self.assertEqual(len(Blog_user.objects.all()),1)

    def test_check_amount_of_blog(self):
        self.assertEqual(len(Blog.objects.all()),1)

    def test_check_amount_of_comment(self):
        self.assertEqual(len(Comment.objects.all()),1)

