# -*- coding: utf-8 -*-

from django.urls import reverse

from django.utils import timezone
from django.contrib.auth.models import User, Group

from .base import BaseTest

class TestSmoke(BaseTest):

    def test_created_user_check(self):
        self.assertEqual(User.objects.count(), 2)

    def test_retrive_without_authentication_token(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 401)

    def test_create_token_and_get_some_authentication(self):
        norm_users_token = self.get_token(self.norm_user.username,
                                            self.norm_user.password,
                                            self.application,
        )

        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(norm_users_token))
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)
