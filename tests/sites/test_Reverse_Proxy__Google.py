from unittest import TestCase

from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Misc import list_set

from serverless_reverse_proxy.sites.Reverse_Proxy__Google import Reverse_Proxy__Google, TARGET_SITE__GOOGLE


class test_Reverse_Proxy__Google(TestCase):

    def setUp(self):
        self.rp_google = Reverse_Proxy__Google()

    def test__init__(self):
        assert self.rp_google.target_site == TARGET_SITE__GOOGLE

    def test_request_get(self):
        response      = self.rp_google.request_get()
        response_text = response.get('text')
        assert list_set(response) == ['content', 'content_type', 'headers', 'json', 'status_code', 'text']

        assert "Google" in response_text