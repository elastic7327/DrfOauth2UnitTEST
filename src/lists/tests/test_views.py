import unittest
from django.test import TestCase


class TestListView(TestCase):

    """Test case docstring."""
    def smokeTest(self):
        self.assertEqual(1, 1, "Hooooray!")
