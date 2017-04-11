from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

MAX_WAIT = 2


class FunctionalTest(StaticLiveServerTestCase):

    """Test case docstring."""

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def smoke_test(self):
        self.assertEqual(1, 1, "Bang!")
