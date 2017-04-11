from .base import FunctionalTest 


class UserViewTest(FunctionalTest):

    def test_list_or_retrive_user_view(self):
        # import ipdb;ipdb.set_trace();
        print(self.browser.get('/'))
