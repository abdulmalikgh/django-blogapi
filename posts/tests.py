from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(
            username = 'testuser', password = 'testuser'
        )
        testuser.save()

        # creating testing object

        test_post = Post.objects.create(
            title = "test title",
            body = "test body",
            author = testuser
        )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        body = f'{post.body}'
        author = f'{post.author}'

        self.assertEqual(title, 'test title')
        self.assertEqual(body, 'test body')
        self.assertEqual(author, 'testuser')

        




