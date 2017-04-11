from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FunctionalTest(StaticLiveServerTestCase):

    """Docstring for FunctionalTest. """
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_smoke(self):
        request = self.browser.get('/sign_up')
        print(request)

    def test_something_test_for_test_test(self):
        request = self.browser.get('/')
        print(request)
