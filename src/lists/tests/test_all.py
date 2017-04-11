# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User, Group


# Create your tests here.

class TestSmoke(TestCase):

    """Test case docstring."""
    def test_create_new_user_and_book(self):
        User.objects.create(first_name="Daniel", last_name="Kim", password="asdfg0")
        self.assertEqual(User.objects.count(), 1)

    def test_create_new_user_and_book_via_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 403)
