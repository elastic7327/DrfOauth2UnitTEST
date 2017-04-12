from datetime import timedelta
from django.urls import reverse

from django.utils import timezone
from django.test import TestCase
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User, Group

from oauth2_provider.models import get_application_model, AccessToken
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.tests.test_utils import TestCaseUtils

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

Application = get_application_model()

class BaseTest(APITestCase, TestCaseUtils):

    """Test case docstring."""

    def setUp(self):
        self.norm_user =  User.objects.create(username='12345', password='12345')
        self.admin_user = User.objects.create(
                                    username="Daniel",
                                    password="as", 
                                    is_superuser=True,
                                    is_staff=True)
        self.application = Application(
                name='lists',
                user=self.admin_user,
                client_type=Application.CLIENT_PUBLIC,
                authorization_grant_type=Application.GRANT_PASSWORD
                )
        self.application.save()

    def tearDown(self):
        pass

    def get_token(self, username, password, application):
         access_user = User.objects.get(username=username)
         access_token = AccessToken.objects.create(
             user=access_user,
             scope='read write',
             expires=timezone.now() + timedelta(seconds=300),
             token=get_random_string(length=128),
             application=application
         )
         return access_token.token
