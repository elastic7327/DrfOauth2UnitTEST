from django.test import TestCase
from lists.models import User 

# Create your tests here.

class TestSmoke(TestCase):

    """Test case docstring."""
    def test_create_new_user_and_book(self):
        User.objects.create(name="Daniel Kim", age=28, occupation="Developer")
        self.assertEqual(User.objects.count(), 1)


    def test_create_new_user_and_book_via_view(self):
        self.create_user(1)
        print(self.NORMALUSER)
